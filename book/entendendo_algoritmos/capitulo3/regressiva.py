def regressiva(i):
    print(i)
    if i <= 0:
        return
    regressiva(i - 1)


regressiva(20)
