class bicicleta:
    def __init__(self, cor, modelo, ano, valor, correndo=True):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.correndo = correndo

    def buzinar(self):
        print("biiiiii")

    def parar(self):
        self.correndo = False
        print("Bicicleta parou")

    def correr(self):
        self.correndo = True
        print("Bicicleta voltou a correr")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
    
    def __del__(self):
        print("Class sendo deletada")

bicicleta_joao = bicicleta("amarelo", "FIAT", 2019, 4000)
bicicleta_joao.parar()
bicicleta_joao.buzinar()
bicicleta_joao.correr()
print(bicicleta_joao)