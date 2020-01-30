word = "bottles"
#No for pode usar o for com o in e com o in range
for beer_num in range(99,0,-1): #range(inicio,parada,de quanto em quanto)
    print(beer_num, word, "of beer on the wall. ")
    print(beer_num,word, "of beer. ")
    print("Take one down. ")
    print("Pass it around. ")
    if beer_num == 1:
        print("No more bottles of beer on the wall. ")
    else:
        new_num = beer_num -1
        if beer_num == 1:
            word = "bottle"
        print(new_num, word, "of beer on the wall. ")
print()