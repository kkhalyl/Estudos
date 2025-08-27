class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def acelerar(self):
        print("Acelerando")

    def frear(self):
        print("Parando")

    
class Carro(Veiculo):
    def abrir_porta(self):
        print("Porta Aberta")
    
    def fechar_porta(self):
        print("Porta Fechada")

class Moto(Veiculo):
    def empinar(self):
        print("Empinando")