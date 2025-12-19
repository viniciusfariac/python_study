def add_binary(a,b):
    return bin(a+b)[:2]
    

a, b = input().split()
print(add_binary(int(a),int(b)))