def breach_attempts(hackers, security_level, increase):
    contador = 0
    for i in hackers: 
        if i > security_level:
            contador += 1
        else:
            security_level += increase
    return contador