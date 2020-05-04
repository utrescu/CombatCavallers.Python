from random import seed
from random import randrange, choice
from llocOnPicar import LlocOnPicar
from ILluitador import ILluitador


class LluitadorRandom(ILluitador):

    def __init__(self, nom):
        self._nom = nom

    def get_nom(self) -> str:
        """retorna el nom del lluitador."""
        return self._nom

    def Protegeix(self) -> list:
        """Llista de llocs on es protegeix"""
        llocs = list(LlocOnPicar)
        llocs.pop(randrange(len(llocs)))
        return llocs

    def Pica(self):
        """Determina on pica el lluitador"""
        pica = choice(list(LlocOnPicar))
        return pica
