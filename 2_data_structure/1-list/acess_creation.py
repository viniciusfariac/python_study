lista = "python"

print(lista[0])
print(lista[-2])


numeros = [1,2,5,8,9,0,5,4,3]
par = []
for numero in numeros:
    if numero % 2 == 0:
       par.append(numero) 

print(par)

pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

matriz = [
    [0,2,3],
    [4,5,6],
    [7,8,9]
]
print(matriz[0][-1])
print(matriz[1][1])
print(matriz[2][0])