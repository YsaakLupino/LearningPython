# Bora calcular a area de um quadrado ou retangulo
# depois multiplicala por valor X inserido pelo usuario)

from time import sleep

#FUNÇÕES

#Efeito Escrever

def Escrever(frase:str, slp:int = 0.05):
    #Printa uma string com efeito de escrita!

    for letra in frase:
        print(letra, end="",flush=True)
        sleep(slp)
    print()


#TEXTOS E VARIÁVEIS

frase_bemvindo = ('\n''Seja bem vindo!!''\n'+
      '\n''Você está no programa de cálculo de àrea!! :)'
      '\n''Diga para mim: Quer calcular a área de um quadrado ou retângul\bo?\n'
      'R: ')

ans_quadouret = None


#CORPO DO CÓDIGO
Escrever(frase_bemvindo, 0.03)


while True:
    try:
        quad_ou_ret = str(input())
        if quad_ou_ret.isdigit():
            raise ValueError
        break
    except ValueError:
        Escrever("Você não inseriu uma resposta válida!\n")


if quad_ou_ret.lower().find("quadrado") >= 0 or quad_ou_ret.lower().find("ret") >= 0:
    if quad_ou_ret.lower().find("quadrado") >= 0:
        ans_quadouret = 0
    else:
        ans_quadouret = 1
else:
    frase_respostaquadnt = ("Não consegui compreender sua resposta! \n"
          "Gostaria de tentar novamente ou prefere sair do programa?\n"
          "(1) Tentar novamente\n"
          "(2) Sair do programa"
          )

    while True:
        Escrever(frase_respostaquadnt)
        try:
            loop_quad = int(input("R: "))
            if 0 < loop_quad < 3:
                if loop_quad == 2:
                    Escrever("Okaay!\n"
                             "Obrigado e xau xau!!"
                            )
                    quit()
                elif loop_quad == 1:
                    continue
                else:
                    raise ValueError
            raise ValueError    
        except ValueError:
            Escrever("Você não inseriu uma resposta válida!")

