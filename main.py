from install import install
from interface.gui import UI
from interface.ui_livro import UILivro  # Ajuste para o nome exato da classe em ui_livro.py
from service.jogo_service import JogoService
from service.livro_service import LivroService
from repository.jogo_repository import JogoRepository
from repository.livro_repository import LivroRepository


def main():
    install()

    # Instâncias de Jogo
    jogo_repository = JogoRepository()
    jogo_services = JogoService(jogo_repository)
    ui_jogo = UI(jogo_services)

    # Instâncias de Livro
    livro_repository = LivroRepository()
    livro_services = LivroService(livro_repository)
    ui_livro = UILivro(livro_services)

    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1. Gerenciar Jogos")
        print("2. Gerenciar Livros")
        print("0. Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            ui_jogo.show_principal_menu()
        elif opcao == "2":
            ui_livro.show_principal_menu()
        elif opcao == "0":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()