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


def busca_media_todas_notas(materia,nota,filtro):
    
    if materia is None or len(materia) == 0:
        return 0
    
    lista_materia = [x for x in materia.split('#')]
    lista_nota = [x for x in nota.split('#')]

    vlr_total = 0
    qtd_total = 0
    for x,i in enumerate(lista_materia):
        if x in (filtro):
            vlr_total += float(lista_nota[i])
            qtd_total += 1
    return vlr_total / qtd_total if ((qtd_total > 0) & (vlr_total > 0)) else 0