paranoid_android = "Marvin, the Paranoid Android"
letters2 = list(paranoid_android)

for char in letters2[:6]:
    print('\t', char)
print()

for char in letters2[-7:]:
    print('\t'*2, char)
print()

for char in letters2[12:20]:
    print('\t'*3, char)
