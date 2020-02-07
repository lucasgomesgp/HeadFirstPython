vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Provide a word to search for vowels: ")
found = []
# Poderia inicializar o dic( valor = [] e depois adicionar novos valores, valor['a'] = 0
valor = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
for letter in word:
    if letter in vowels:
        if letter == 'a':
            valor['a'] += 1
        elif letter == 'e':
            valor['e'] += 1
        elif letter == 'i':
            valor['i'] += 1
        elif letter == 'o':
            valor['o'] += 1
        else:
            valor['u'] += 1
        if letter not in found:
            found.append(letter)
# # Se ficar desordenado usa-se a função sorted, for vowel in sorted(valor)
# for vowel in valor:
#     print(vowel, " apareceu", valor[vowel], " vez(es)")
#k - key , v - value
for k, v in sorted(valor.items()):
    print(k, "apareceu ",v," vez(es)")
print(valor)
