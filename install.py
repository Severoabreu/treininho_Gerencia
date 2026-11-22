from database.connection import get_connection

def install():
    connection = get_connection()

    try:
        cur = connection.cursor()
        # Entidade 1
        # Criar tabela no banco de dados
        connection.execute("""
            CREATE TABLE IF NOT EXISTS livro(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                autor TEXT,
                lido INTEGER NOT NULL DEFAULT 0
            )
            """)
        cursor = connection.execute("SELECT COUNT(*) FROM livro")
        total_livros = cursor.fetchone()[0]
        
        if total_livros == 0:
            connection.execute(
                "INSERT INTO livro (titulo, autor, lido) VALUES (?, ?, ?)",
                ("paranormal", "Ronaldo", 0)
                )
    
        # Inserir dados iniciais (OBRIGATÓRIO!!!!)
        
        
        # Entidade 2
        connection.execute("""""")
        
        
        # Entidade 3
        connection.execute("""
            CREATE TABLE IF NOT EXISTS jogo (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome VARCHAR UNIQUE NOT NULL,
                preco FLOAT NOT NULL,
                lancado BOOLEAN DEFAULT TRUE
            )
        """)

        cur.execute("SELECT COUNT(*) FROM jogo")
        if cur.fetchone()[0] == 0:
            connection.executemany("""
                INSERT INTO jogo (nome, preco, lancado)
                VALUES (?, ?, ?);
            """, [
                ('GTA VI', 499.99, True),
                ('Hollow Knight Silksong: Sea of Sorrow', 100.50, False),
                ('Terraria', 37.99, True)
            ])
        
        
        connection.commit()

    finally:
        connection.close()


if __name__ == "__main__":
    install()
    print("Banco de dados instalado com sucesso.")