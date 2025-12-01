def ola_mundo(nome):
    return print(f"Olá mundo {nome}")

def ola_longo(nome):
    print(f"Olá longo {nome}")

def executar(funcao, nome):
    return funcao(nome)

executar(ola_longo, "Vinicius")
executar(ola_mundo, "Vinicius")