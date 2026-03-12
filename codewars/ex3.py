def is_prime(num):
    numeros = []
    for i in range(1, num + 1):
        if num % i == 0 and i > 0:
            numeros.append(i)
    return "is prime" if len(numeros) > 2 else "is not prime"
        

print(is_prime(2))