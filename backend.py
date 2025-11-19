from api_controller import fetch_user_activity, count_user_activit
import json

def menu_print():
    print("O que deseja fazer?")
    print("1 - Realizar pesquisa")
    print("2 - Sair")

def menu():
    while True:
        menu_print()
        escolha = int(input("Digite a opção: "))

        if escolha == 1:
            """user = input("Digite o usuário: ")"""

            degbug = "JoaoGRSilva"

            events = fetch_user_activity(degbug)
            print(events)
            activity = count_user_activit(events)
            print(json.dumps(activity, indent = 4))

        if escolha == 2:
            print("Encerrando...")
            break

        else:
            print("Opção incorreta.")