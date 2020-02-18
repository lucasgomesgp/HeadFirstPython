class CountFromBy:
    # dunder init, é um dos métodos mágicos
    # self -> é o argumento inicial padrão dos métodos, ele faz um papel parecido com o this
    # -> indica qual vai ser o retorno, neste caso da função ___init__ ela não retorna nada
    def __init__(self, v: int = 0, i: int = 1) -> None:
        #Com o self o atributo sobrevive depois da função encerrar, não mantém o escopo de função
        self.val = v
        self.incr = i

    def increase(self) -> None:
        self.val += self.incr
    #O dunder __repr__ controla como um objeto é exibido
    def __repr__(self):
        return str(self.val)
    
