import os
os.chdir('/home/lucas/Downloads/HeadFirstPython/Cap12')

with open('buzzers.csv') as raw_data:
    #O read() -> Consome todos os dados do arquivo de uma vez.
    print(raw_data.read())