from install import install
from interface.gui import UI
from service.jogo_service import JogoService
from repository.jogo_repository import JogoRepository

def main():
    install()

    repository = JogoRepository()
    services = JogoService(repository)
    UI(services).show_principal_menu()



if __name__ == "__main__":
    main()