import sys

try:
    1/0
except:
    #exec_info() -> fornece informações sobre a execução que está sendo tratada 
    err = sys.exec_info()
    for e in err:
        print(e)