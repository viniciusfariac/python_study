voted = {}
def verificarEleitor(eleitor):
    if (voted.get(eleitor)):
        print("Vai embora")
    else:
        print("Pode votar")
        voted[eleitor] = True

verificarEleitor("Vinicius")
verificarEleitor("Vinicius")
verificarEleitor("Raphaella")