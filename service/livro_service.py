from repository.livro_repository import LivroRepository
from entities.livro import Livro


class LivroService:

    def __init__(self, repository):
        self.repository = repository

    def create(self, titulo, autor):
        if not titulo or not titulo.strip():
            raise ValueError("O titulo do livro é obrigatório")

        novo_livro = Livro(
            titulo=titulo.strip(),
            autor=autor.strip() if autor else "",
            lido=False
        )
        return self.repository.create(novo_livro)

    def list(self):
        pass

    def get(self, task_id):
        pass

    def update(self, task_id, title, description):
        pass

    def delete(self, task_id):
        pass