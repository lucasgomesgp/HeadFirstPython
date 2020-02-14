# O with não precisa fechar(close()) e ele faz o mesmo papel de todos = open('test.txt')

with open('test.txt') as tasks:
    for chore in tasks:
        print(chore, end='')
