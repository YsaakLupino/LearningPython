class organizada:
    def __init__(self):
        self.inicio = None
    
    class no:
        def __init__(self,atual):
            self.atual = atual
            self.proximo = None
    
    def addend(self, atual): #adicionar no final
        dado = organizada.no(atual)  
        if self.inicio != None:
            temp = self.inicio
            while temp.proximo != None:
                temp = temp.proximo
            temp.proximo = dado
            return dado
            
        self.inicio = dado
        return dado
    
    def exibir(self): #exibir sua lista
        temp = self.inicio
        if self.inicio == None:
            raise IndexError('Lista vazia')
        print('[', end='')
        while temp.proximo != None:
            print(f'{temp.atual}', end=', ')
            temp = temp.proximo
        print(f'{temp.atual}]')
    
    def addini(self, atual): #adicionar no inicio
        dado = organizada.no(atual)
        temp = self.inicio
        self.inicio = dado
        self.inicio.proximo = temp
        
    def removini(self):
        temp = self.inicio.proximo
        self.inicio = temp
    
    def removend(self):
        temp = self.inicio
        while temp.proximo.proximo != None:
            temp = temp.proximo
        print(temp.atual)
        temp.proximo = None

    def removeval(self, n):
        temp = self.inicio
        while True:
            if temp.atual == n:
                self.inicio = temp.proximo
                break
            temp2 = temp
            temp = temp.proximo
            while True:
                if temp.atual == n:
                    temp = temp.proximo
                    temp2.proximo = temp
                    break
                temp2 = temp
                temp = temp.proximo
            break
    
    def removepstn(self, p):
        temp = self.inicio
        while True:
            cont = 1
            if p == cont:
                self.inicio = temp.proximo
                break
            temp2 = temp
            temp = temp.proximo
            cont += 1
            while True:
                if p == cont:
                    temp = temp.proximo
                    temp2.proximo = temp
                    break
                temp2 = temp
                temp = temp.proximo
                cont += 1
                break
            break
             

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
lista.exibir()
