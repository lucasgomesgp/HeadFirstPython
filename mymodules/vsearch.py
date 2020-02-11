# :str - indica o tipo do valor e -> set tipo de estrutura de retorno, nesse caso sendo o conjunto
# As três aspas duplas chamam-se docstring -> """ """
def search4vowels(phrase: str) -> set:
    """Return any vowels found in an asked-for word"""
    print('Chamada de Funcão')
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


def search4letters(phrase: str, leterrs: str = 'aeiou') -> set:
    """ Return a set of the 'letters' found in 'phrase'."""
    return set(leterrs).intersection(set(phrase))
