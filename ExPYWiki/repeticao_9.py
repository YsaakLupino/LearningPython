'''
Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
'''

odd = []
pair = []
for num in range(1, 51):
    if num%2 != 0:
        odd.append(num)
    else:
        pair.append(num)

for count, num in enumerate(odd, start=1):
    print(num, flush=True, end="")
    if count == len(odd):
        print(".")
        break
    print("; ", flush=True, end="")
