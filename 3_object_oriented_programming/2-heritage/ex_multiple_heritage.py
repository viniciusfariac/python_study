class animal:
    def __init__(self, nro_pata):
        self.nro_pata = nro_pata

class mamifero(animal):
    def __init__(self, nro_pata, cor_pelo):
        super().__init__(nro_pata=nro_pata)
        self.cor_pelo = cor_pelo
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
    
class gato(mamifero):
    def __init__(self, nro_pata, cor_pelo, domestico=True):
        super().__init__(nro_pata, cor_pelo)
        self.domestico = domestico

gato_pedro = gato(4, "preto")
print(gato_pedro)