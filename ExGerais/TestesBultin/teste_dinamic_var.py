
#apesar de "b = a", ao troca valor de "a", b continua com o valor de set
a = 1
print(a)
b = a
print(b)
a = 2 
print(a)
print(b)

# solução caso eu queria uma variavel que copia o valor de outra, porem fazendo com função

#COM DEF
y = 1
def x():
    return y
print(y)
print(x())
y = 2
print(y)
print(x())

#COM LAMBDA
z = 1
v = lambda: z
print(z)
print(v())
z = 2
print(z)
print(v())