#python 023
n = str(input("Por favor digite um número de 0 À 9999: "))


#### jeito str 

n_com_0 = f"{n:0>4}"
n_com_0_1 = format(n,"0>4")
n_com_0_2 = '{:0>4}'.format(n)

print(f"""
Unidades: {n_com_0[3]}
Dezenas : {n_com_0_1[2]}
Centenas: {n_com_0_2[1]}
Milhares: {n_com_0_1[0]}      
""")

#jeito int

u = int(n) // 1 % 10
d  = int(n) // 10 % 10
c = int(n) // 100 % 10
m = int(n) // 1000 % 10



print(f"""
Unidades: {u}
Dezenas:  {d}
Centenas: {c}
Milhares: {m}      
""")