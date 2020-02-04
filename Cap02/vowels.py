#Criação e atribuição dos valores na lista
vowels = ['a','e','i','o','u']

word = "Milliways"

#Verificar se as letras presentes em word estão nas vowels/vogais
for letter in word:
    if letter in vowels:
        print(letter)