from maksukortti import Maksukortti


HINTA = 5


class Kassapaate:
    def __init__(self):
        self.__myytyja_lounaita = 0

    def lataa(self, kortti: Maksukortti, summa: int):
        kortti.lataa(summa)

    def osta_lounas(self, kortti: Maksukortti):
        if kortti.saldo() >= HINTA:
            kortti.osta(HINTA)
            self.__myytyja_lounaita = self.__myytyja_lounaita + 1
