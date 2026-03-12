def monkey_count(n):
    #your code here
    numbers = []
    for i in range(n):
        numbers.append(i+1)
    return numbers

def monkey_count_simple(n) :
    return list(range(1, n + 1))

print(monkey_count(10))
print(monkey_count_simple(11))