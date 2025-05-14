array = [11,15,2,7]
target = 9


for idx, p1 in enumerate(array,0):
    if p1 > 9:
        continue
    lf_num = 9 - p1
    for idx2, p2 in enumerate(array[idx+1:], idx+1):
        if p2 == lf_num:
            resultado = (idx, idx2 )
        
print(resultado)
            



# solução em O(2n²+1)