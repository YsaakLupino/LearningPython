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
            temp = self.head
            while temp.proximo != None:
                temp = temp.proximo
            temp.proximo = dado
            return
            
        self.head = dado

    
    def exibir(self): # Exibir sua lista
        temp = self.head
        if self.head == None:
            raise IndexError('Lista vazia') 
        print('[', end='') # Parte visual para parecer uma lista de python
        while temp.proximo != None:
            print(f'{temp.atual}', end=', ')
            temp = temp.proximo
        print(f'{temp.atual}]')
    
    def addini(self, dado): #adicionar nó antes do head
        dado = organizada.no(dado)
        temp = self.head
        self.head = dado
        self.head.proximo = temp # não necessita de if lista vazia
        
    def removini(self): #Remover primeiro nó
        if self.head == None:
            raise IndexError('Lista Vazia') # controle erro contra lista vazia 
        temp = self.head.proximo
        self.head = temp
    
    def removend(self): #Remover ultimo nó
        if self.head == None:
            raise IndexError('Lista Vazia') # controle erro contra lista vazia 
        temp = self.head
        while temp.proximo.proximo != None:
            temp = temp.proximo
        print(temp.atual)
        temp.proximo = None

    def removeval(self, valor): # Remover nó por seu valor atual
        if self.head == None:
            raise IndexError('Lista Vazia') # controle erro contra lista vazia 
        temp = self.head
        while True:
            if temp.atual == valor:
                self.head = temp.proximo
                break
            temp2 = temp # Guardando temp anterior ao do valor a ser removido para atualizar seu proximo depois
            temp = temp.proximo
            while True:
                try: # Tratando erro caso nao exista o valor na lista
                    if temp.atual == valor:
                        temp = temp.proximo
                        temp2.proximo = temp
                        break
                    temp2 = temp
                    temp = temp.proximo
                except AttributeError:
                    break # Simplesmente nao acontece nada caso o elemento nao exista na lista
            break
    
    def removepstn(self, pstn):
        temp = self.head
        cont = 0
        if pstn == cont: #caso o primeiro no ja o procurado
            self.head = temp.proximo 
            return
        temp2 = temp
        temp = temp.proximo
        cont += 1
        try: # Tratando erro caso posição nao exista! 
            while True:
                if pstn == cont:
                    temp = temp.proximo
                    temp2.proximo = temp
                    break
                temp2 = temp
                temp = temp.proximo
                cont += 1
        except AttributeError:
            return # Nada acontece caso a posição não exista!



#Testes a se fazer:

'''
Adicionar função print atraves de dunder methods
'''
'''
Adicionar parametro de posição 1 2 3.. ao removini e removendo
'''  

lista = organizada()
lista.addend(1)
lista.addend(2)
lista.addend(3)
lista.addend(4)
lista.exibir()
lista.removeval(4)
lista.exibir()
lista.addend(4)
lista.addend(5)
lista.exibir()
lista.removeval(4)
lista.exibir()
lista.removeval(3)
lista.exibir()
lista.removepstn(1)
lista.exibir()
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
lista.removepstn(1)
lista.exibir()

lista2 = organizada()

lista2.addini(12)
lista2.addini(121)
lista2.removeval(121)
lista2.exibir()