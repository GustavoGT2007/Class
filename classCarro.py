class Carro:

    def __init__ (self,cor,modelo,ano,nivelOleo):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.nivelOleo = nivelOleo

    def ligar(self):
        print("O carro esta ligado")
    
    def acelerar(self):
        print("O carro esta acelerando")

    def frear(self):
        print("O carro esta freado")
        self.__nivelOleo(self.nivelOleo)

    def __nivelOleo(self,nivelOleo):
        if nivelOleo <= 3:
            print(" ** IMPORTANTE ** Verificar o nivel de óleo")

carroFox = Carro("Preto","Fox","1857",2)

print(carroFox.ano)
print(carroFox.acelerar())