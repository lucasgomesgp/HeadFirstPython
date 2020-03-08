
from pprint import pprint
from datetime import datetime

def converter2ampm(time24: str) -> str:
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')

with open('buzzers.csv') as data:
    ignore = data.readline() # Ignora o cabeçalho
    flights = {}
    for line in data:
        #strip() exclui os espaços do começo ao final
        k, v = line.strip().split(',')
        flights[k] = v

pprint(flights)
print()

flights2 = {}
for k,v in flights.items():
    flights2[converter2ampm(k)] = v.title
pprint(flights2)
print()

fts = {converter2ampm(k): v.title() for k,v in flights.items()}
pprint(fts)
print()

#DICTCOMP,SETCOMP,LISTCOMP
when = {dest: [k for k,v in fts.items() if v == dest] for dest in set(fts.values())}
pprint(when)
print()