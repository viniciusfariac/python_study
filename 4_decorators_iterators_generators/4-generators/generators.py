def my_generator(list: list[int]):
    for numero in list:
        yield numero * 2
    

for i in my_generator([1,2,3,4,5,6]):
    print(i)