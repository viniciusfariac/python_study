def buscaMenor (arr: list):
    menor = arr[0]
    menor_indice = 0

    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    return menor_indice


def ordenacaoporSelecao (arr: list):
    novoArr = []

    for i in range (len(arr)):
        menor = buscaMenor(arr)
        novoArr.append(arr.pop(menor))
    return novoArr


print(ordenacaoporSelecao([2,1,2,3,5,3,6,8,94,5,6,7,8,9,4,2,1]))