

class UILivro:
    
    def __init__(self, livro_services):
        self.livro_services = livro_services
        
    def ler_id(self):
        try:
            return int(input("Informe o ID do livro: "))
        except ValueError:
            raise ValueError("O ID deve ser um número inteiro válido. ")
        
    def show_principal_menu(self):
        
        while True:
            print("\n=== CATÁLOGO DE livros ===")
            print("1 - Cadastrar livro")
            print("0 - sair")
            
            opcao = input("Escolha uma opção: ").strip()
            
            try :
                if opcao == "1":
                    titulo = input("Titulo do livro: ")
                    autor = input("Autor do livro: ")
                    novo_id = self.services.create(titulo, autor)
                    print(f"livro cadastrado com sucesso! ID gerado: {novo_id}")
                    
                
                elif opcao == "0":
                    print("Saindo...")
                    break
                
                else:
                    print ("Opção  inválida. ")
            
            except  ValueError as erro:
                print(f"Erro: {erro}")
                    
                    