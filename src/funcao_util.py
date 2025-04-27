import unicodedata

def remove_acentos(texto):
    """
    Remove acentos de um texto.
    """
    if texto is None:
        return None
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

def minha_funcao():
    return "Teste"