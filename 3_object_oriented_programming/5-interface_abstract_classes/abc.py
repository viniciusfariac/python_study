from abc import ABC, abstractmethod

class Animal(ABC):

    coracao = True

    def __init__(self):
        pass

    @abstractmethod
    def animal_info(self):
        pass

    @abstractmethod
    def animal_part(self):
        pass


class mamifero(Animal):
    def __init__(self, nome):
        self.nome = nome

    def animal_info(self):
        return print(self.nome)

    def animal_part(self):
        return print("AAAA")


leao = mamifero("Leão")

leao.animal_info()
leao.animal_part()