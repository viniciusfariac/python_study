class Aluno:
    escola = "Vinicius School"

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def __str__(self):
        return f"nome: {self.nome} idade: {self.idade} escola: {self.escola}"

def mostrar_todos(*objs):
    for obj in objs:
        print(obj)

nathan = Aluno("Nathan", 16)
joao = Aluno("Jão", 17)
print(nathan, joao)

joao.nome = "João"
Aluno.escola = "p"

mostrar_todos(nathan, joao)