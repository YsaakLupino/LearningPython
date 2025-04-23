#python 011

largura = float(input('Qual a largura da parede que irá pintar?\nR: '))
altura = float(input('Qual a altura da parede que irá pintar?\nR: '))
tinta = altura*largura/2

print('Considerando que a parade tem {} M² de área e cada litro de tinta pinta 2m² de parede, '
      'você precisará de {:.1f} litros de tinta'.format(largura*altura, tinta))

