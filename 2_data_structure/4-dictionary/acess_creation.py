pessoa = {"nome": "Vinicius Faria", "Idade": 17, "Estudando python?": True}

print(pessoa)
print(pessoa["nome"])

pessoas = {
    "Vinicius Faria": {"idade": 17, "Hobby": "Estudar", "Estuda python?": True},
    "Ana Maria": {"idade": "15", "Hobby": "Ler", "Estuda": False},
    "Jota Marinho": {"idade": 31, "Hobby": "Pescar", "Trablha": True}
}

print(pessoas)
print(pessoas["Vinicius Faria"])
print(pessoas["Jota Marinho"]["idade"])


for chave, valor in pessoas.items():
    print(chave, valor)

for chave, valor in pessoas.items():
    for chave, valor in valor.items():
        print(chave, valor)