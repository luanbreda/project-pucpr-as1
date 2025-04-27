import pytest
from src.funcao_util import remove_acentos, busca_maior_nota, calcular_media

def test_remove_acentos_lowercase():
    assert remove_acentos("áéíóúãõâêîôû") == "aeiouaoaeiou"

def test_remove_acentos_uppercase():
    assert remove_acentos("ÁÉÍÓÚÃÕÂÊÎÔÛ") == "AEIOUAOAEIOU"

def test_remove_acentos_special_characters():
    assert remove_acentos("ç") == "c"

def test_remove_acentos_empty_string():
    assert remove_acentos("") == ""

def test_remove_acentos_sem_acentos():
    assert remove_acentos("aeiou") == "aeiou"
    assert remove_acentos("AEIOU") == "AEIOU"

def test_busca_maior_nota():
    assert busca_maior_nota("10#9#8") == 10.0
    assert busca_maior_nota("5#6#7") == 7.0
    assert busca_maior_nota("0#0#0") == 0.0
    assert busca_maior_nota("10#10#10") == 10.0
    assert busca_maior_nota("10#9#8#7#6#5") == 10.0
    assert busca_maior_nota("5#6#7#8#9#10") == 10.0

def test_calcular_media():
    assert calcular_media("Matematica#Portugues#Historia", "10#9#8", "Matematica") == 10.0
    assert calcular_media("Matematica#Portugues#Historia", "0#0#0", "Historia") == 0.0
    assert calcular_media("Matematica#Portugues#Historia#Matematica#Matematica", "5#10#10#5#5", "Matematica") == 5.0
    assert calcular_media("Historia#Historia#Historia#Historia", "8#6#2#4") == 5.0
    assert calcular_media("Matematica#Portugues#Historia", "10#0#2", "Portugues") == 0.0


