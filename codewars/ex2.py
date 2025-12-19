def sum_two_smallest_numbers(numbers: list):
    a = min(numbers)
    numbers.remove(a)
    b = min(numbers)
    numbers.remove(b)
    return a + b

number = [1,2,3,4,5]

print(sum_two_smallest_numbers([19, 5, 42, 2, 77]))

# or


def sum_two_smallest_numbers(numbers: list):
    return sum(sorted(numbers)[:2])

print(sum_two_smallest_numbers([19, 5, 42, 2, 77]))