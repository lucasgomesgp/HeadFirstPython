vowels = set('aeiou')
word = input("Provide a word to search for vowels: ")
found = {}
# set() -> transforma em conjunto
found = vowels.intersection(set(word))

for letter in found:
    print(letter)
