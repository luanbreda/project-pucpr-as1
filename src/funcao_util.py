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

def busca_maior_nota(nota):
    
    numeros = list(map(int, nota.split("#")))
    if len(numeros) == 0:
        return 0
    
    return max(numeros)


def busca_media_todas_notas(materias_str, notas_str, filtro=None):
    # Dividir as strings em listas
    materias = materias_str.split("#")
    notas = list(map(float, notas_str.split("#")))

    # Criar um dicionário associando matérias às notas
    notas_por_materia = dict(zip(materias, notas))

    # Se um filtro for aplicado, calcular apenas para a matéria específica
    if filtro and filtro in notas_por_materia:
        return notas_por_materia[filtro]
    
    # Caso contrário, calcular a média geral
    return sum(notas) / len(notas)