class Organizada:
    def __init__(self):
        self.head = None #Head
        self.len = 0
    
    class No:
        def __init__(self,atual):
            self.atual = atual
            self.proximo = None
    
    #Funções:
    def add_end(self, dado): # Adicionar nó ao final da lista
        dado = Organizada.No(dado) 
        if self.head != None:
            node_pointer = self.head
            while node_pointer.proximo != None:
                node_pointer = node_pointer.proximo
            node_pointer.proximo = dado
            self.len += 1
            return
            
        self.head = dado
        self.len += 1

    
    def show(self): # Exibir sua lista
        node_pointer = self.head
        if self.head == None:
            raise IndexError('Lista vazia') 
        print('[', end='') # Parte visual para parecer uma lista de python
        while node_pointer.proximo != None:
            print(f'{node_pointer.atual}', end=', ')
            node_pointer = node_pointer.proximo
        print(f'{node_pointer.atual}]')
    
    def add_ini(self, dado): #adicionar nó antes do head
        dado = Organizada.No(dado)
        node_pointer = self.head
        self.head = dado
        self.head.proximo = node_pointer # não necessita de if lista vazia
        self.len += 1
        
    def remov_ini(self): #Remover primeiro nó
        if self.head == None:
            raise IndexError('Lista Vazia') # controle erro contra lista vazia 
        node_pointer = self.head.proximo
        self.head = node_pointer
        self.len -= 1
    
    def remov_end(self): #Remover ultimo nó
        if self.head == None:
            raise IndexError('Lista Vazia') # controle erro contra lista vazia 
        node_pointer = self.head
        if node_pointer.proximo == None:
            self.head = None
            self.len -= 1
            return
        while node_pointer.proximo != None:
            node_pointer2 = node_pointer
            node_pointer = node_pointer.proximo
        node_pointer2.proximo = None
        self.len -= 1

    def remov_val(self, valor): # Remover nó por seu valor atual
        if self.head == None:
            raise IndexError('Lista Vazia') # controle erro contra lista vazia 
        node_pointer = self.head
        if node_pointer.atual == valor:
            self.head = node_pointer.proximo
            self.len -= 1
            return
        node_pointer2 = node_pointer # Guardando node_pointer anterior ao do valor a ser removido para atualizar seu proximo depois
        node_pointer = node_pointer.proximo
        try: # Tratando erro caso nao exista o valor na lista
            while True:
                if node_pointer.atual == valor:
                    node_pointer2.proximo = None
                    self.len -= 1
                    break
                node_pointer2 = node_pointer
                node_pointer = node_pointer.proximo
                
        except AttributeError:
            return # Simplesmente nao acontece nada caso o elemento nao exista na lista
            
    
    def remove_pos(self, pstn):
        if pstn < 0: # Caso a pstn seja menor que 0 ele remove de frente para trás!
            node_pointer = self.head
            cont = 1
            while node_pointer.proximo != None:
                node_pointer = node_pointer.proximo
                cont += 1
            pstn = cont + pstn
        node_pointer = self.head
        cont = 0
        if pstn == cont: #caso o primeiro no ja o procurado
            self.head = node_pointer.proximo 
            self.len -= 1
            return
        node_pointer2 = node_pointer
        node_pointer = node_pointer.proximo
        cont += 1
        try: # Tratando erro caso posição nao exista!
            while True: 
                if pstn == cont:
                    node_pointer2.proximo = None
                    self.len -= 1
                    return
                node_pointer2 = node_pointer
                node_pointer = node_pointer.proximo
                cont += 1     
        except AttributeError:
            return # Nada acontece caso a posição não exista!

    def count(self):
        return self.len
        

#Testes a se fazer:

'''
Adicionar função print atraves de dunder methods
'''
'''
Adicionar parametro de posição 1 2 3.. ao removini e removend
'''  

lista = Organizada()
lista.add_end(1)
lista.add_end(2)
lista.add_end(2)
lista.add_end(2)
lista.add_end(2)
lista.add_end(2)
lista.remov_end()
lista.remov_end()
lista.remove_pos(0)
lista.show()
print(lista.count())

lista2 = Organizada()
lista2.add_ini(12)
lista2.add_ini(121)
lista2.add_ini(12)
lista2.show()
lista2.remov_val(12)
lista2.show()
lista2.remov_val(12)
lista2.show()
print('Sua lista tem, atualmente,',lista2.count(),'elementos!')
