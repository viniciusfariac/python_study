class Animal:
    def comendo(self):
        return print("NHAQUE")

class Leao(Animal):
    def comendo(self):
        return print("AHWAHW")

class Leoa(Animal):
    def comendo(self):
        return super().comendo()

def plano_comendo(obj):
    return obj.comendo()


leao = Leao()
leoa = Leoa()
plano_comendo(leao)
plano_comendo(leoa)