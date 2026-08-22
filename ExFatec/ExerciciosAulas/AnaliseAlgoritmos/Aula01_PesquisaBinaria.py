
import timeit


#SEARCHING CONFIGURATIONS
listt = list(range(1,1_000_000)) #1 to 1 million test list 
search_value = 100
#-----------------------------------------------------------


#funções de bbusca
def binary_search(vetor:list[int],value:int) -> tuple[int,int|str,int]:
    '''
    manual implementation of a binary search for studies
    '''
    
    down = 0
    upper = len(vetor)-1
    middle = (upper + down) // 2

    interations_count = 0
    # vetor = sorted(vetor)

    while down <= upper:
        interations_count += 1
        if value == vetor[middle]:
            return (vetor[middle], middle,interations_count)
        
        elif value > vetor[middle]:
            down = middle + 1
        elif value < vetor[middle]:
            upper = middle -1
        middle = (upper + down) // 2

    return (value,"Valor não existe no vetor",interations_count)

def linear_search(vetor:list[int],value:int) -> tuple[int,int|str,int]:
    interations_count = 0
    for n,item in enumerate(vetor,0):
        interations_count += 1
        if value == item:
            return (vetor[n],n,interations_count)
    return (value,"Valor não existe no vetor",interations_count)
    
#========================================================================

if __name__ == "__main__":
    tempo_binary = timeit.timeit(
        lambda: binary_search(listt, search_value),
        number=10
    )
    tempo_linear = timeit.timeit(
        lambda: linear_search(listt, search_value),
        number=10
    )

    print(f"Tempo médio: {(tempo_binary / 10) * 1_000_000:.3f} µs")
    print(f"Tempo médio: {(tempo_linear / 10) * 1_000_000:.3f} µs")

