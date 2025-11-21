pessoas = {
    "Vinicius Faria": {"idade": 17, "Hobby": "Estudar", "Estuda python?": True},
    "Ana Maria": {"idade": "15", "Hobby": "Ler", "Estuda": False},
    "Jota Marinho": {"idade": 31, "Hobby": "Pescar", "Trablha": True}
}

print(pessoas)
copia = pessoas.copy()
copia["Vinicius Faria"] = {"idade": 16}
print(copia["Vinicius Faria"])
print(pessoas["Vinicius Faria"])
dict.fromkeys(["nome", "tel"])
print(pessoas.get("chave", "Sem dados"))
print(pessoas.clear())