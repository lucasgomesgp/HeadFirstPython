# TUPLA - Usa () e LISTA - Usa[]
vowels = ['a', 'e', 'i', 'o', 'u']
vowels2 = ('a', 'e', 'i', 'o', 'u')
print(type(vowels))
print(type(vowels2))

vowels[2] = 'I'
#Não roda porque a Tupla é imutável
vowels2[2] = 'I'

print(vowels)
print(vowels2)
