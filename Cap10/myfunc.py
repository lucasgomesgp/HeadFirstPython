#O operador * (*args) -> faz a função aceitar uma lista de argumentos
def myfunc(*args):
    for a in args:
        print(a, end=' ')
    if args:
        print()

"""
    Com o operador ** ele pega a chave e o valor,
    como um dicionário. 
    Ex: conn = mysql.connector.connect(**dbconfig)

"""
#kw- seria key-words
def myfunc2(**kwargs):
    for k,v in kwargs.items():
        print(k, v, sep='->', end=' ')
    if kwargs:
        print()

def myfunc3(*args,**kwargs):
    if args:
        for a in args:
            print(a ,end=' ')
        print()
    if kwargs:
        for k,v in kwargs.items():
            print(k, v, sep='->', end=' ')
        print()