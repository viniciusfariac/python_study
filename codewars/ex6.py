def digital_root(n):
    while len(str(n)) > 1:
        lista = []
        for i in str(n):
            lista.append(int(i))
        n = sum(lista)

    return n
    
    
        


print(digital_root(100))