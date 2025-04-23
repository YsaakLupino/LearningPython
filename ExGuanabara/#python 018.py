#python 018

from math import cos, sin, tan, radians

angulo = float(input('Qual o angulo que voce deseja calcular? '))

radianos = radians(angulo)


print('Referente ao ângulo {0}°:\nEm radianos: {4:>11.2f}\nO COSSENO vale: {2:>8.2f}\nO SENO vale: {1:>11.2f}'
      '\nA TANGENTE vale: {3:>7.2f}'.format(angulo, sin(radianos), cos(radianos), tan(radianos), radianos))