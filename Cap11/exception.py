#Sempre importante capturar e TRATAR a exceção
try:
    with open('test.txt') as fh:
        file_data = fh.read()
    print(file_data)
    
#Só é executado caso o arquivo test.txt não exista
except FileNotFoundError:
    print("The data file is missing.")
except PermissionError:
    print("This is not allowed.")
#Exceção genérica
except Exception as err:
    print("Some other error occurred", str(err))
