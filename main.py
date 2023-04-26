import todo_manager

def print_menu():
    menu = [
        "1. Criar lista",
        "2. Imprime detalhes da lista",
        "3. Salve os dados no arquivo",
        "Z. Sair",
        "Digite uma opção"
    ]
    for valor in menu:
        print(valor)

def main():
    print("Bem vindo")
    while True:
        print_menu()
        opcao = input(">>>  ")
        if opcao == "1":
            todo_manager.criar_um_todo()
        elif opcao == "2":
            todo_manager.ler_lista()
        elif opcao == "2":
            todo_manager.salvar()
        elif opcao == "Z":
            print("Obrigado por usar o nosso sistema.")
            break

if __name__ == "__main__":
    main()
