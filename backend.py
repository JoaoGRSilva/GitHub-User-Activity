from api_controller import fetchUserActivity

def menu_print():
    print("O que deseja fazer?")
    print("1 - Realizar pesquisa")
    print("2 - Sair")

def menu():
    while True:
        menu_print()
        escolha = int(input("Digite a opção: "))

        if escolha == 1:
            user = input("Digite o usuário: ")
            response = fetchUserActivity(user)
            print(response)

        if escolha == 2:
            print("Encerrando...")
            break

        else:
            print("Opção incorreta.")