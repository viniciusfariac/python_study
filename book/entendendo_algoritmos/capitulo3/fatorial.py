def fat(x):
    if x == 1:
        return x
    return x * fat(x-1)
 

print(fat(2))