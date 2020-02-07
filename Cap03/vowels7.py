vowels = {'a', 'e', 'i', 'o', 'u'}
vowels2 = set('aeeiouu')
word = 'helo'
u = vowels.union(set(word))
d = vowels.difference(set(word))
i = vowels.intersection(set(word))

print("UNIÃO: ", u)
print("DIFERENÇA: ", d)
print("INTERSECÇÃO: ", i)
