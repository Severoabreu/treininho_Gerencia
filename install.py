from database.connection import get_connection

def install():
    connection = get_connection()

    try:
        
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
<<<<<<< HEAD
        #conection.execute("""""")
        
        
        # Entidade 3
        #connection.execute("""""")
=======
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
>>>>>>> 03817c7958e8d6a2f5777d34bfb4464453074c2f
        
        
        connection.commit()

    finally:
        connection.close()


if __name__ == "__main__":
    install()
    print("Banco de dados instalado com sucesso.")