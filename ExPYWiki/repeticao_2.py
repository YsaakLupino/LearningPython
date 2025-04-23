'''
Faça um programa que leia um nome de usuário e a sua senha 
e não aceite a senha igual ao nome do usuário, mostrando 
uma mensagem de erro e voltando a pedir as informações.
'''

while True:
    USER = str(input("Insira um nome de usuário: "))
    PASSWORD = str(input('Insira uma senha: '))
    if USER == PASSWORD:
        print('A senha e o usuário não podem ser iguais!')
        continue
    print('usuário e senha válidos!')
    break
