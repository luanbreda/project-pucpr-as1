from funcao import *

def test_remove_acentos():
    assert remove_acentos("áéíóúãõâêîôû") == "aeiouaeiou"
    assert remove_acentos("çãõ") == "cao"
    assert remove_acentos("áéíóúãõâêîôûçãõ") == "aeiouaeioucao"


def test_remove_acentos_empty():
    assert remove_acentos("") == ""
    assert remove_acentos(None) == None
    assert remove_acentos(" ") == " "
    assert remove_acentos("a") == "a"
    assert remove_acentos("á") == "a"