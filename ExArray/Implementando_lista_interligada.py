class organizada:
    def __init__(self):
        self.head = None #Head
    
    class no:
        def __init__(self,atual):
            self.atual = atual
            self.proximo = None
    
    #Funções:
    def addend(self, dado): # Adicionar nó ao final da lista
        dado = organizada.no(dado) 
        if self.head != None:
            node_pointer = self.head
            while node_pointer.proximo != None:
                node_pointer = node_pointer.proximo
            node_pointer.proximo = dado
            return
            
        self.head = dado

    
    def show(self): # Exibir sua lista
        node_pointer = self.head
        if self.head == None:
            raise IndexError('Lista vazia') 
        print('[', end='') # Parte visual para parecer uma lista de python
        while node_pointer.proximo != None:
            print(f'{node_pointer.atual}', end=', ')
            node_pointer = node_pointer.proximo
        print(f'{node_pointer.atual}]')
    
    def addini(self, dado): #adicionar nó antes do head
        dado = organizada.no(dado)
        node_pointer = self.head
        self.head = dado
        self.head.proximo = node_pointer # não necessita de if lista vazia
        
    def removini(self): #Remover primeiro nó
        if self.head == None:
            raise IndexError('Lista Vazia') # controle erro contra lista vazia 
        node_pointer = self.head.proximo
        self.head = node_pointer
    
    def removend(self): #Remover ultimo nó
        if self.head == None:
            raise IndexError('Lista Vazia') # controle erro contra lista vazia 
        node_pointer = self.head
        while node_pointer.proximo.proximo != None:
            node_pointer = node_pointer.proximo
        print(node_pointer.atual)
        node_pointer.proximo = None

    def removeval(self, valor): # Remover nó por seu valor atual
        if self.head == None:
            raise IndexError('Lista Vazia') # controle erro contra lista vazia 
        node_pointer = self.head
        while True:
            if node_pointer.atual == valor:
                self.head = node_pointer.proximo
                break
            node_pointer2 = node_pointer # Guardando node_pointer anterior ao do valor a ser removido para atualizar seu proximo depois
            node_pointer = node_pointer.proximo
            while True:
                try: # Tratando erro caso nao exista o valor na lista
                    if node_pointer.atual == valor:
                        node_pointer = node_pointer.proximo
                        node_pointer2.proximo = node_pointer
                        break
                    node_pointer2 = node_pointer
                    node_pointer = node_pointer.proximo
                except AttributeError:
                    break # Simplesmente nao acontece nada caso o elemento nao exista na lista
            break
    
    def removepstn(self, pstn):
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
            return
        node_pointer2 = node_pointer
        node_pointer = node_pointer.proximo
        cont += 1
        try: # Tratando erro caso posição nao exista! 
            while True:
                if pstn == cont:
                    node_pointer = node_pointer.proximo
                    node_pointer2.proximo = node_pointer
                    break
                node_pointer2 = node_pointer
                node_pointer = node_pointer.proximo
                cont += 1
        except AttributeError:
            return # Nada acontece caso a posição não exista!
    
    def count(self):
        node_pointer = self.head
        if node_pointer == None:
            return 0
        cont = 1    
        while node_pointer.proximo != None:
            node_pointer = node_pointer.proximo
            cont += 1
        return cont
    
        

#Testes a se fazer:

'''
Adicionar função print atraves de dunder methods
'''
'''
Adicionar parametro de posição 1 2 3.. ao removini e removend
'''  

lista = organizada()
lista.addend(1)
lista.addend(2)
lista.addend(3)
lista.addend(4)
lista.show()
lista.removeval(4)
lista.show()
lista.addend(4)
lista.addend(5)
lista.show()
lista.removeval(4)
lista.show()
lista.removeval(3)
lista.show()
lista.removepstn(1)
lista.show()
lista.addend(6)
lista.addend(7)
lista.addend(8)
lista.addend(9)
lista.addend(10)
lista.removini()
lista.addini(4)
lista.addini(3)
lista.addini(2)
lista.addini(1)
lista.removepstn(12)
lista.removepstn(-2)
lista.show()
print('Sua lista tem, atualmente,',lista.count(),'elementos!')

lista2 = organizada()

lista2.addini(12)
lista2.addini(121)
lista2.removeval(12)
lista2.removeval(121)
print('Sua lista tem, atualmente,',lista2.count(),'elementos!')