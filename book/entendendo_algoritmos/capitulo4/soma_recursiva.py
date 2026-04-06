# def soma_valores (lista: list, soma):
#     if (len(lista) == 0):
#         print(soma)
#         return soma
    
#     soma += lista.pop()
#     print(soma, lista)
#     soma_valores(lista, soma)

# soma_valores([1,2,3,4,5], 0)

def soma_valores (lista: list):
    if (lista == []):
        return 0
    
    print(lista[1:])
    return lista[0] + soma_valores(lista[1:])

print(soma_valores([1,2,3,4,5]))