from time import time

listt = list(range(1,1_000_001)) #1 to 1 million test list 
print(listt)

def binary_search(vetor:list[int],value:int) -> bool|int:
    '''
    manual implementation of a binary search for studies
    '''
    minor = 0
    upper = 