
'''
Farei aqui uma breve análise do algoritmo de busca linear contra busca binária

Sempre será buscado o último item da lista, que será o pior caso para ambos os 
algoritmos, para testar com efetividade

Além disso, para cálculo de tempo, foi classe timeit da biblioteca timeit
que, recebe uma função como parametro e um numero inteiro, ela roda aquela função 
o numero de vezes que voce passou nesse inteiro e retorna o tempo total de execução.
Assim podemos calcular a média dessas execuções e chegar a um valor mais preciso, do que
apenas testar a função uma unica vez.

Digo ainda, que, para fins de teste, admitisse que os vetores já estão ordenados
e contem apenas um tipo de dados ( Números inteiros) 

A analise englobará 2 graficos e uma tabela

GRÁFICO 1 
TEMPO X TAMANHO DA LISTA (MOSTRARÁ A CURVA DE CRESCIMENTO DE TEMPO DE EXECUÇÃO COM AMBOS ALGORTIMOS)

GRÁFICO 2 
INTERAÇÕES X TAMANHO DA LISTA (MOSTRA A CURVA EM RELACIONADA A NOTAÇÃO BIG O)

** Para os gráficos 1 e 2 o eixo x terá 7 tamanhos diferentes de lista, começando
em 10 elementos e terminando em 10 milhões de elementos


Tabela de comparação por posição 
(MOSTRA EM QUE MOMENTO UM ALGORITMO PASSA A SER MELHOR QUE O OUTRO
	Para esta tabela o tamnho da lista será fixo em 10000 elementos
    O intuito aqui é visualizar em que momento um algoritmo passa a
    ter vantagem sobre outro além de mensurar essa vantagem.

Formato da tabela:
posição       linear    binária    vantagem
1             0.3 ms    0.5 ms     linear 18×
10            0.5 ms    1.5 ms     linear 11×
100           2 ms      1.75 ms     linear 2.7×
1000          20 ms     2.5 ms     binária 3.6×
'''

#=================CÓDIGO DE BUSCA LINEAR E BINÁRIA=========================
import timeit


#BENCHMARK SEARCHING CONFIGURATIONS-----------------------------------------
def get_last_value(vetor:list[int]) -> int:
    '''
    Função para pegar o útltimo valor da lista, 
    Assim testando os algoritmos no pior dos casos!
    '''
    return vetor[-1]

listt_len = [10,100,1000,10000,100000,
            1_000_000,10_000_000] #Teste com varios tamanhos de lista

listt_position =[1,10,50,100,500,1000] #Teste de busca em varias posições da lista



def get_interations(vetor:list[int],value:int) -> tuple[int,int]:
    '''
    Função para pegar o numero de interações quando busca x valor em y vetor
    para cada um dos algoritmos
    '''
    iter_binary = binary_search(vetor,value)[1]
    iter_linear = linear_search(vetor,value)[1]
    return (iter_linear,iter_binary)

#-----------------------------------------------------------


#funções de bbusca
def binary_search(vetor:list[int],value:int) -> tuple[int|str,int]:
    '''
    manual implementation of a binary search for studies
    '''
    
    down = 0
    upper = len(vetor)-1
    middle = (upper + down) // 2

    interations_count = 0
    

    while down <= upper:
        interations_count += 1
        if value == vetor[middle]:
            return (middle,interations_count)
        
        elif value > vetor[middle]:
            down = middle + 1
        elif value < vetor[middle]:
            upper = middle -1
        middle = (upper + down) // 2

    return ("Valor não existe no vetor",interations_count)

def linear_search(vetor:list[int],value:int) -> tuple[int|str,int]:
    interations_count = 0
    for n,item in enumerate(vetor,0):
        interations_count += 1
        if value == item:
            return (n,interations_count)
    return ("Valor não existe no vetor",interations_count)
    
#========================================================================

if __name__ == "__main__":


    for tamanho in 
    tempo_binary = timeit.timeit(
        lambda: binary_search(listt, search_value),
        number=10
    )/10
    tempo_linear = timeit.timeit(
        lambda: linear_search(listt, search_value),
        number=10
    )/10

    print(f"Tempo médio: {(tempo_binary) * 1_000_000:.3f} µs")
    print(f"Tempo médio: {(tempo_linear) * 1_000_000:.3f} µs")

