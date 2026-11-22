from database.connection import get_connection

def install():
    connection = get_connection()

    try:
        
        # Entidade 1
        # Criar tabela no banco de dados
        connection.execute("""""")

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
        
        
        connection.commit()

    finally:
        connection.close()


if __name__ == "__main__":
    install()
    print("Banco de dados instalado com sucesso.")