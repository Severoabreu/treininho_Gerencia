from database.connection import get_connection
from entities.livro import Livro

class LivroRepository:
    
    def create(self, livro):
        conn = get_connection()
        
        try:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO livro (titulo, autor, lido) VALUES (?, ?, ?)",
                (livro.titulo, livro.autor, int(livro.lido))
                )
            conn.commit()
            return  cursor.lastrowid
        
        finally :
            conn.close()
    
    
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
    
    