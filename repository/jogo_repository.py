from database.connection import get_connection
from entities.jogo import Jogo

class JogoRepository:
    def __init__(self) -> None:
        self.conn = get_connection()

    def create(self, jogo: Jogo):
        # Inserir no banco
        try:
            cur = self.conn.cursor()

            cur.execute(f"""
                INSERT INTO jogo (nome, preco, lancado)
                VALUES ('{jogo.nome}', {jogo.preco}, {jogo.lancado})
            """)

            cur.execute("SELECT id FROM jogo LIMIT 1")
            jogo_id = cur.fetchone()[0]

            return jogo_id

        except Exception:
            self.conn.rollback()
        finally:
            self.conn.close()

    def find_all(self):
        # Consultar todas as entidades
        pass

    def find_by_id(self, task_id):
        # Consultar pelo ID
        pass

    def update(self, task):
        # Atualizar
        pass

    def delete(self, task_id):
        # Excluir
        pass