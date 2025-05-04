'''
Ao receber o input de uma lista de int, o programa deve identificar qual a maior
squencia formada dentro do array e em seguida contar quantos elementos tem 
(o comprimento dessa sequencia). Ele retorna este dado.

Exemplo:
    Input = [1,4,6,23,5,2,9,11]
    Output = 3 pois a maior sequencia é [4,5,6] e o tamanho é de 3 elementos
'''

nums = [1,0,4,3,23,45,46,47,48,49,50,51,52,5,2,9,11]
nums_dict = {}
sequence_lenght = 1
for num in nums:
    nums_dict[num] = num
print(nums_dict)

for num in nums:
    if num-1 not in nums_dict:
        sequence_lenght_temp = 1
        while num+1 in nums_dict:
            sequence_lenght_temp += 1
            num+=1
        if sequence_lenght_temp >= sequence_lenght:
            sequence_lenght = sequence_lenght_temp

print(sequence_lenght)

'''
eu compreendi que o melhor jeito nao era percorrer ele varias vezes mas nao
consegui fazer sozinho, eu peguei a ideia da solução no video mas a codagem eu desenvolvi
'''

'''
Como desafio ficam os outros 2 problemas
 do vídeo https://www.youtube.com/watch?v=sjqB70KIfog
'''


    