class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    @staticmethod
    def maior_idade(nome, idade):
        return idade >= 18
    
    @classmethod
    def mostrar_idade(cls, nome, data_nascimento):
        return f"idade: {2025 - data_nascimento}, nome: {nome}"
    
print(Pessoa.mostrar_idade("Vinicius", 2008))
print(Pessoa.maior_idade("Vinicius", 17))