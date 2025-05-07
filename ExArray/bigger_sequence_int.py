"""Exercícios video - agusto galego.

3 problemas que mais caem em entrevistas do vídeo https://www.youtube.com/watch?v=sjqB70KIfog

    1) Ao receber o input de uma lista de int, o programa deve identificar qual a maior
squencia formada dentro do array e em seguida contar quantos elementos tem 
(o comprimento dessa sequencia). Ele retorna este dado.

Exemplo:
Input = [1,4,6,23,5,2,9,11]
Output = 3 pois a maior sequencia é [4,5,6] e o tamanho é de 3 elementos

    2) Dado um array de ints 'nums' e um inteiro 'K' retorne o(s) k elemento(s) mais
frequente(s) na lista

Exemplo:
Input = [1,1,1,2,2,3,3]
K = []
"""
class Exercicios():
    """Representa exercicios do vídeo."""

    def __init__(self):
        """Setter classe Exercícios."""
        pass

    def exercício_1(self, nums_list:list[int]) -> int:
        """Realiza execução do exercício 1.

        Printa o resultado do exercicio

        Args:
            nums_list (list[int]): Lista a analisar
        
        Returns:   
            tudo
            none      
        """
        nums = nums_list
        nums_dict = {}
        sequence_lenght = 1
        for num in nums:
            nums_dict[num] = num

        for num in nums_dict:
            if num-1 not in nums_dict:
                sequence_lenght_temp = 1
                while num+1 in nums_dict:
                    sequence_lenght_temp += 1
                    num+=1
                if sequence_lenght_temp >= sequence_lenght:
                    sequence_lenght = sequence_lenght_temp
        print(f'A maior sequencia da lista tem o tamanho de {sequence_lenght} números')

