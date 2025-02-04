import pytest

from ..utils.afficher_tout import affiche_tout_tache
from app import task

def test_affichetache (): 
    assert task == "Aucune tâche enregistrée."