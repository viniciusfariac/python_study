def unique_in_order(sequence):
    lista = []
    for i in range(len(sequence)):
        if sequence[i] != sequence[i - 1] or sequence[i] not in lista:
            lista.append(sequence[i])
    return lista
print(unique_in_order("ABBBBBBBBBBCCCCCCCCCAAAAAAAAAFFFFFFFFF"))