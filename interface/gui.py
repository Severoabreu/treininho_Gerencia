from service.jogo_service import JogoService

class UI:

    def __init__(self, jogo_service: JogoService):
        self.jogo_service = jogo_service

    def show_principal_menu(self):
        # Exibir opções
        # Receber escolha do usuário
        # Chamar os métodos do service
        print("""
        Jogos:
        1. criar jogo
        2. listar jogos
        3. buscar jogo (por id)
        4. atualizar jogo
        5. excluir jogo
        """)

        opc = int(input("escolha (1-5): "))
        match opc:
            case 1:
                nome = input("insira o nome: ")
                preco = float(input("insira o preco: "))
                lancado = input("ja foi lancado? (S/n): ").lower() == "n"

                resultado = self.jogo_service.create(nome, preco, lancado)

                if resultado[0] is not None:
                    print(resultado[1])
                    print(f"id do jogo: {resultado[0]}")
                else:
                    print(resultado[1])

            case _:
                print("erro")