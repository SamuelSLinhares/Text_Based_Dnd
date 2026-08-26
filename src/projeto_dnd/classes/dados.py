from random import randint

def d20(qtd):
    res = 0
    for i in range(qtd):
        res += randint(1,20)
    return res
    
def d12(qtd):
    res = 0
    for i in range(qtd):
        res += randint(1,12)
    return res

def d10(qtd):
    res = 0
    for i in range(qtd):
        res += randint(1,10)
    return res

def d8(qtd):
    res = 0
    for i in range(qtd):
        res += randint(1,8)
    return res

def d6(qtd):
    res = 0
    for i in range(qtd):
        res += randint(1,6)
    return res

def d4(qtd):
    res = 0
    for i in range(qtd):
        res += randint(1,4)
    return res

def d2(qtd):
    res = 0
    for i in range(qtd):
        res += randint(1,2)
    return res 