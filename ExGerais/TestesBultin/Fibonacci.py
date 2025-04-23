um = 0
dois = 1
Phi = int(input('Até que posição do Phi voce quer ver? '))
#tres = False

for n in range(Phi):
    if n == 0:
        print(f"Posição {n+1}: '{n}'")
        continue
    if n == 1:
        print(f"Posição {n+1}: '{n}'")
        continue
    tres = um + dois
    print(f"Posição {n+1}: '{tres}'")
    um = dois
    dois = tres
