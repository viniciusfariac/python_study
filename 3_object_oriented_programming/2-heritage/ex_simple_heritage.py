class veiculo:
    def __init__(self, cor, roda, placa):
        self.cor = cor
        self.roda = roda
        self.placa = placa

    def ligar(self):
        return print("MOTOR LIGANDOOOO")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f"{chave}={valor}" for chave, valor in self.__dict__.items()])}"
    
class motocicleta(veiculo):
    def __init__(self, cor, roda, placa, nome):
        super().__init__(cor, roda, placa)
        self.nome = nome

class moto(veiculo):
    pass
class carro(veiculo):
    pass

motociclete_pedro = motocicleta("preto", "2", "abc", "MOTOLANDA")

print(motociclete_pedro.cor)
motociclete_pedro.ligar()
print(motociclete_pedro)