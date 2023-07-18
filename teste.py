class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class Arvore:
    def __init__(self, raiz):
        self.raiz = No(raiz)

    def preordenar(self, inicio, lista):
        if inicio is not None:
            lista.append(inicio.valor) #raiz
            lista = self.preordenar(inicio.esquerda, lista)
            lista = self.preordenar(inicio.direita, lista)
        return lista
    
    def posordenar(self, inicio, lista):
        if inicio is not None:
            print('lista demo 1:', lista)
            lista = self.posordenar(inicio.esquerda, lista)
            print('lista demo 2:', lista)
            lista = self.posordenar(inicio.direita, lista)
            print('lista demo 3:', lista)
            lista.append(inicio.valor)
        return lista

arvore1 = Arvore(1)

arvore1.raiz.esquerda = No(3)
arvore1.raiz.direita = No(5)

arvore1.raiz.esquerda.esquerda = No(7)
arvore1.raiz.esquerda.direita = No(9)

print(arvore1.preordenar(arvore1.raiz.esquerda, []))
#print(arvore1.posordenar(arvore1.raiz, []))

