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