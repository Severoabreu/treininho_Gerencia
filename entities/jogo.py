class Jogo:
    def __init__(
        self,
        id: int | None = None,
        nome: str = "",
        preco: float = 0,
        lancado: bool = True
    ):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.lancado = lancado
