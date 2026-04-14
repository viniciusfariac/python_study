def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivo = arr[0]
        menores = [i for i in arr[1:] if i <= pivo]
        maiores = [i for i in arr[1:] if i > pivo]
        print(f"pivo: {pivo} menores: {menores} maiores {maiores}")
        return quicksort(menores) + [pivo] + quicksort(maiores)

print(quicksort([10, 5, 3, 2, 1, 4]))