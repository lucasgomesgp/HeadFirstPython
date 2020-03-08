
import pprint

with open('buzzers.csv') as data:
    ignore = data.readline() # Ignora o cabeçalho
    flights = {}
    for line in data:
        #strip() exclui os espaços do começo ao final
        k, v = line.strip().split(',')
        flights[k] = v
pprint.pprint(flights)