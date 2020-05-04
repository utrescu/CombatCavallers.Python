from random import randint
from ILluitador import ILluitador
from Resultat import *
from typing import List

IResultList = List[float]


class Ring:
    VIDAINICIAL = 20

    def EntradaLluitadors(self, lluitador1, lluitador2):
        """Els dos lluitadors entren al Ring"""
        primer = Resultat(lluitador1, Ring.VIDAINICIAL)
        segon = Resultat(lluitador2, Ring.VIDAINICIAL)
        self._Lluitadors = [primer, segon]

    def Lluiteu(self) -> IResultList:
        """Combat entre els dos lluitadors"""

        if len(self._Lluitadors) != 2:
            print("ERROR. Falten lluitadors")
            exit

        elQuePica = randint(0, 1)

        while self._Lluitadors[0].es_Ko() == False and self._Lluitadors[1].es_Ko() == False:
            elQueRep = (elQuePica+1) % 2
            proteccio = self._Lluitadors[elQueRep].get_Lluitador().Protegeix()
            pica = self._Lluitadors[elQuePica].get_Lluitador().Pica()

            if pica in proteccio:
                self._Lluitadors[elQueRep].treu_vida()
                print(
                    f'{self._Lluitadors[elQueRep].get_nom()} rep un cop al {pica.name} de {self._Lluitadors[elQuePica].get_nom()}')
            else:
                print(
                    f'{self._Lluitadors[elQueRep].get_nom()} atura el cop al {pica.name} de {self._Lluitadors[elQuePica].get_nom()}')
            elQuePica = elQueRep

        guanyador = next(x for x in self._Lluitadors if x.es_Ko() == False)
        perdedor = next(i for i in self._Lluitadors if i.es_Ko() == True)

        comentariLocutor = ""

        if (guanyador.get_vida() - perdedor.get_vida()) > 5:
            comentariLocutor = "Quina pallissa!!"

        print(f"{perdedor.get_nom()} cau a terra!")
        print(f"VICTÒRIA DE {guanyador.get_nom()}!!! {comentariLocutor}")

        return self._Lluitadors
