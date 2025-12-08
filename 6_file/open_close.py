file = open("6_file/files/exemp.txt", "w")
# print(file.read())
# print("uma linha: ", file.readline())
# print(file.readlines())
file.write("DIGITANDO NO ARQUIVO")
for i in ["Eu","Estou","Testando"]:
    file.writelines(f"\n{i}")
file.close()