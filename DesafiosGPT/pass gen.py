'''
Exercícios de Lógica e Estruturas

Gerador de senhas
Implemente uma função que gere senhas seguras com comprimento variável, contendo letras maiúsculas, minúsculas, números e caracteres especiais.
➝ Extra: permita definir regras (ex: mínimo de 2 números, 1 símbolo etc.).

Compressão RLE (Run-Length Encoding)
Implemente a compressão RLE:

Entrada: "aaabbcccc"

Saída: "a3b2c4"
➝ Extra: crie também a função de descompressão.

Sudoku Validator
Escreva uma função que receba uma matriz 9x9 e verifique se é uma solução válida de Sudoku.

Números Felizes
Verifique se um número é feliz. Um número feliz é aquele que, somando os quadrados de seus dígitos repetidamente, chega a 1.
'''

def pass_gen(min, max=None):
    '''
    MIN : Tamanho minimo da senha
    MAX: tamanho maximo da senha
        (SE NAO PREENCHIDA A SENHA TERA O TAMANHO MÍNIMO)
    '''

    import random
    
    if min < max:
        PASS_LENGHT = random.randint(min, max)
        print('tamanho :', PASS_LENGHT)
    else:
        PASS_LENGHT = min

    alfabeto = [
        'a','b','c','d','e','f','g','h','i','j','k','l','m',
        'n','o','p','q','r','s','t','u','v','w','x','y','z',
        'A','B','C','D','E','F','G','H','I','J','K','L','M',
        'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
    ]

    # Caracteres especiais
    caracteres_especiais = [
        '!','@','#','$','%','^','&','*','(',')',
        '-','_','=','+','[',']','{','}',';',':',
        "'",'"','\\','|',',','.','<','>','/','?','`','~'
    ]

    # Números
    numeros = ['0','1','2','3','4','5','6','7','8','9']
    print(PASS_LENGHT)

pass_gen(1)

