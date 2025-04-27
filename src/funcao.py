
import unicodedata

def remove_acentos(texto):
    if texto:
        return ''.join(c for c in unicodedata.normalize('NFKD', texto) if not unicodedata.combining(c))
    return texto