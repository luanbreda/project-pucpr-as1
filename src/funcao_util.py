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

def busca_maior_nota(string):
    numeros = list(map(int, string.split("#")))
    return max(numeros)

def calcular_media(materias_str, notas_str, filtro=None):
    materias = materias_str.split("#")
    notas = list(map(float, notas_str.split("#")))

    # Criar um dicionário associando matérias às notas
    notas_por_materia = dict(zip(materias, notas))

    if filtro and filtro in notas_por_materia:
        return notas_por_materia[filtro]

    # Calcular a média sem arredondar automaticamente para cima
    media = sum(notas) / len(notas)
    
    return round(media, 2)  # Arredonda para duas casas decimais