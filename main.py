from install import install
from interface.gui import UI
from service.services import Services
from repository.dao_entity import DAOEntity

def main():
    install()

    repository = DAOEntity()
    services = Services(repository)
    UI(services).show_principal_menu()



if __name__ == "__main__":
    main()