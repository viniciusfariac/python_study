def banco(*dados_banco, **dados_pessoal):
    return print(f'Dados do banco: {dados_banco}\nDados pessoal: {dados_pessoal}')

banco("Bradesco", "Criado em 2021", "Criador: Vinicius", nome="Vinicius Faria", idade=17, profissao="Eng Software")

# No "TODO", abaixo: Crie a função 'soma_tupla' para receber uma tupla de números inteiros como argumento:

def todo(tupla):
    return sum(tupla)

if __name__ == "__main__":
    entrada = input()
# No "TODO", abaixo: Defina tupla para receber os números inteiros:
    elementos = todo(map(int, entrada.split()))
    
    resultado = todo(elementos)
    print(f"A soma dos elementos da tupla é: {resultado}")