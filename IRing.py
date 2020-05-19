from Resultat import *
from typing import List

IResultList = List[float]

class IRing:

    def EntradaLluitadors(self, lluitador1, lluitador2):
        """Els dos lluitadors entren al Ring"""
        pass

    def Lluiteu(self) -> IResultList:
        """Es fa el combat"""
