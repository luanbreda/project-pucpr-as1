import pytest
from src.funcao_util import remove_acentos

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