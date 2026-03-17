def high_and_low(numbers: str):
    numbers = numbers.split()
    n = []
    for i in range(len(numbers)): n.append(int(numbers[i]))
    n.sort()
    return f"{n[-1]} {n[0]}" 



# def high_and_low(numbers):
#     numbers = sorted(numbers.split(), key=int)
#     return f"{numbers[-1]} {numbers[0]}" 

print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))