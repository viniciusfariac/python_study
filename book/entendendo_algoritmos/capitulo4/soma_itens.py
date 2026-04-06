def soma(lista:list):
    maior = lista[0]
    if (len(lista) == 1):
        print(maior)
        return maior
    
    if (lista[0] > lista[1]):
        lista.pop(1)
        soma(lista)
    else:
        lista.pop(0)
        soma(lista)


soma([1,2,3,4,1,2,3,4])