class calcular_numeros:
    def __init__(self, numeros: list[int]):
        self.numeros = numeros
        self.contador = 0
    
    def __iter__(self):
        return self

    def __next__(self):
        try:
            numero = self.numeros[self.contador]
            self.contador += 1
            resultado = numero * 2
            return resultado
        except IndexError:
            raise StopIteration
        

for i in calcular_numeros(numeros=[1,2,3,5]):
    print(i)