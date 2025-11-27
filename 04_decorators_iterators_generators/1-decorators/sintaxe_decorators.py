def teste(funcao):
    def teste2():
        print("Teste 2")
        funcao()
        print("AAAAAAAAAAAAA")

    return teste2

@teste
def teste3():
    print("Teste3")


teste3()