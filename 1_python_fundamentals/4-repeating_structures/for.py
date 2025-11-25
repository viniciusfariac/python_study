texto = input("Informe um texto: ").lower()
VOGAIS = "aeiou"

for i in texto:
    if i in VOGAIS:
        print(i, end=" ")
else:
    print()
    print("Executado no final do laço")

for numero in range(0, 51, 5):
    print(numero, end=" ")


# for min in range(9, -1, -1):
#     for seg in range(59, -1, -1):
#         print(f"{min}:{seg}")