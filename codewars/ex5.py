import math
# def series_sum(n):
#     # Happy Coding ^_^
#     if n == 0:
#         return "0.00"
    
#     valor = 1
#     n = n * 3
#     for i in range(1, n):
#         div = 1 / ((1 + 3) * float(i))
#         valor += div

#     return f"{valor:.2f}"

def series_sum(n):
    # Happy Coding ^_^
    valor = 0.0
    for i in range(0, n):
        valor += 1 / (1 + 3 * float(i))

    return f"{valor:.2f}"

print(series_sum(0))
print(series_sum(1))
print(series_sum(2))
print(series_sum(3))
print(series_sum(4))
print(series_sum(5))
        
    # numbers = [1.00]
    # i = 4
    # for i in range(10):
    #     if n == n:
    #         return numbers 
        
    #     n = sum(numbers) + (1/i)
    #     numbers.append(1/i)