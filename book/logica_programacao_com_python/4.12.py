from dataclasses import dataclass

@dataclass
class reg_estudantes:
    Nome: str
    Nota: float
    Media: float


equipe = [None] * 4
for i in range(4):
    equipe[i] = reg_estudantes("", [0,0,0,0], 0)


for i in range(4):
    equipe[i].Nome = input("Digite seu nome: ")
    for j in range(4):
        equipe[i].Nota[j] = int(input(f"Digite sua {j + 1} nota: "))
    media = sum(equipe[i].Nota) / 4
    equipe[i].Media = media

print(equipe)
