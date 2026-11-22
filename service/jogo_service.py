from repository.jogo_repository import JogoRepository
from entities.jogo import Jogo

class JogoService:

    def __init__(self, repository: JogoRepository):
        self.repository = repository

    def create(self, nome, preco, lancado):
        # Validar dados (MUITO IMPORTANTE!!!!!)
        # Criar entidade
        # Solicitar persistência
        if nome.strip() == "" or nome is None:
            raise ValueError("nome invalido")

        if preco < 0 or preco is None:
            raise ValueError("preco invalido")

        jogo = Jogo(nome=nome, preco=preco, lancado=lancado)

        try:
            jogo_id = self.repository.create(jogo)

            return (jogo_id, "operacao realizada com sucesso")
        except Exception:
            return (None, "operacao falhou")

    def list(self):
        pass

    def get(self, task_id):
        pass

    def update(self, task_id, title, description):
        pass

    def delete(self, task_id):
        pass