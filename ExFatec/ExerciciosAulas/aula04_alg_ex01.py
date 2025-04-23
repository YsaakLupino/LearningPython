n1 = float(input('Insira a primeira nota do aluno: '))
n2 = float(input('Insira a segunda nota do aluno: '))

media = (0.4*n1)+(0.6*n2)

if media >= 5.0:
    print("O aluno foi aprovado!")
else:
    print("O aluno foi Reprovado!")

print("A média foi de {}".format(media))