class Lexer:
    digitos = "0123456789"

    def __init__(self, texto):
        self.indice = 0
        self.tokens = []
        self.token = None
        self.texto = texto
        self.char = self.texto[self.indice]

    def move(self):
        self.indice += 1
        if self.indice < len(self.texto):
            self.char = self.texto[self.indice]

    def tokenizar(self):
        while self.indice < len(self.texto):
            if self.char in Lexer.digitos:
                self.token = self.extrair_numero()
            
        self.tokens.append(self.token)


    def extrair_numero(self):
        numero = ""
        while(self.char in Lexer.digitos) and (self.indice < len(self.texto)):
            print(numero)
            numero += self.char
            self.move()
        return Inteiro(numero)

class Token:
    def __init__(self, valor, tipo):
        self.valor = valor
        self.tipo = tipo

    def __repr__(self):
        return self.valor
    
class Inteiro(Token):
    def __init__(self, valor):
        super().__init__(valor, "INT")


a = Lexer("123")
a.tokenizar()
print(a.tokens)