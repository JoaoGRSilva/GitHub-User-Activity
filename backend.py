from api_controller import fetch_user_activity, count_user_activit, activit_treatment
import json, os

clear = lambda: os.system('cls')

def menu_print():
    print("O que deseja fazer?")
    print("1 - Realizar pesquisa")
    print("2 - Sair\n")

def menu():
    while True:
        menu_print()
        escolha = int(input("Digite a opção: "))

        if escolha == 1:
            """user = input("Digite o usuário: ")"""
            events = fetch_user_activity("JoaoGRSilva")
            counters = count_user_activit(events)
            activit_treatment(events, counters)

        if escolha == 2:
            print("Encerrando...")
            break

        else:
            print("Opção incorreta.")