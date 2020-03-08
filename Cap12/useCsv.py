import csv

with open('buzzers.csv') as data:
    #csv.reader(data) -> Lê um de cada vez, o csv.DictReader(data)-> Lê um por vez e transforma em dicionário
    for line in csv.DictReader(data):
        print(line)