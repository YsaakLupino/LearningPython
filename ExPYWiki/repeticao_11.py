'''
Altere o programa anterior para mostrar no final a soma dos números.
'''

while True:
    try:
        n1 = int(input('Digite o primeiro número: '))
        break
    except ValueError:
        print("Entrada Inválida")

while True:
    try:
        n2 = int(input('Digite o segundo número: '))
        break
    except ValueError:
        print("Entrada Inválida")
nums = [n1, n2]
nums_to_sum = []
for num in range (min(nums), max(nums)+1):
    print(num, flush= True, end="")
    nums_to_sum.append(num)
    if num == max(nums):
        print(".")
        break
    print('; ', flush= True, end="")

print(f'A soma dos números é: {sum(nums_to_sum)}')
