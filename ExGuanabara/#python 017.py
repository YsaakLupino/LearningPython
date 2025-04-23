#python 017
from math import hypot


# com modulo math

c1 = float(input('Qual a medida do cateto oposto? '))
c2 =float(input('Qual a medida do cateto adjacente? '))

print('A hipotenusa deste triângulo equivale à: {:.2f}'.format(hypot(c1,c2)))

#matematicamente 

c1 = float(input('Qual a medida do cateto oposto? '))
c2 =float(input('Qual a medida do cateto adjacente? '))
hyp = (c1**2+c2**2)**(1/2)

print('A hipotenusa deste triângulo equivale à: {:.2f}'.format(hyp))
