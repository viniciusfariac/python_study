a = {1,2}
b = {2,3,5}

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(b.difference(a))
print(a.symmetric_difference(b))
print(a.issubset(b))
print(a.issuperset(b))
print(a.isdisjoint(b))

sorteio = {1,24,25}
sorteio.add(28)
sorteio.copy()
sorteio.discard(1)
print(sorteio)
sorteio.pop()
print(sorteio)