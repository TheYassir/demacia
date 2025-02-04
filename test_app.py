import pytest
import affiche_tache
from app import task

def test_affichetache (): 
    assert task == "Aucune tâche enregistrée."