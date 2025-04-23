#python 028

from random import randint

print("Vou pensar em um número de 0 a 5, tente adivinhar!!")
n = randint(0,5)
r= int(input("Qual número voce acha que eu pensei?\nR: "))

if r == n:
    print("Parabéns você acertou!!")
else:
    print("Poxa... Você errou, tente novamente!")