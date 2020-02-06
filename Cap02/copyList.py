first = [1,2,3,4,5]
# Entrega o endereço de memória e ambos apontam para o mesmo objeto
second = first

second.append(6)

# A maneira correta de copiar uma lista
third = second.copy()
third.append(7)
print(first, second)
print(third)
# [Começo:Parada:De quanto em quanto] START/STOP/STEP
print(first[0:2:1])
print(first[2:])
print(first[:2])
print(first[::4])

#Os últimos 2 elementos
print(first[-2:])