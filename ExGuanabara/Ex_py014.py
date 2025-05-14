#python 034
salario = float(input("Qual o salário do funcionario? "))

if salario > 1250.00:
    salario *= 1.10
else:
    salario *= 1.15

print(f"Seu novo salário é de R${salario:.2f}")