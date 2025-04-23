# importações

import sys
from time import sleep
import random

# funções


def menu():
    print("(1) Jogar\n(2) Regras\n(3)Sair do jogo")
    while True:
        try:
            input_menu = int(input("O que deseja fazer?\nR: "))
            break
        except ValueError or TypeError:
            print("por favor escolha o numero de uma das opções")
    while True:
        try:
            if input_menu > 3 or input_menu < 1:
                print("por favor escolha o numero de uma das opções")
                input_menu = int(input("O que deseja fazer?\nR: "))
            else:
                break
        except ValueError:
            pass
    return input_menu


def regras():
    print('você rola um par de dados, obtendo um valor entre 2 e 12:\n')
    sleep(2)
    print('Se na primeira jogada você tirar 7 ou 11 você recebe um "natural" e ganhou.\n')
    sleep(2)
    print('Se você tirar 2, 3 ou 12 na primeira jogada isto é chamado de "craps" e você perdeu.\n')
    sleep(2)
    print('Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10, este é seu "Ponto"\n')
    sleep(2)
    print('Seu objetivo agora é continuar jogando os dados até tirar este número novamente.\n')
    sleep(2)
    print('Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.\n')
    replay_regras()


def replay_regras():
    while True:
        try:
            ver_regras = int(input("Deseja ver as regras novamente?\n"
                                   "(1) Não, voltar ao menu!\n"
                                   "(2) Sim, por favor!\nR: "))
            break
        except ValueError:
            print("Escolha uma das opções listadas")
    if ver_regras == 1:
        menu()
    elif ver_regras == 2:
        regras()
    else:
        print("Escolha uma das opções listadas")
        replay_regras()

regras()