from time import time

listt = list(range(1,501)) #1 to 1 million test list 


def binary_search(vetor:list[int],value:int) -> bool|int:
    '''
    manual implementation of a binary search for studies
    '''
    
    down = 0
    upper = len(vetor)-1
    middle = round (upper-down/2)
    vetor = sorted(vetor)

    while True:
        if value == vetor[middle]:
            return middle
        elif value > vetor[middle]:
            down = middle + 1
        elif value < vetor[middle]:
            upper = middle -1

        middle = round (upper-down/2)

print(binary_search(listt,120))