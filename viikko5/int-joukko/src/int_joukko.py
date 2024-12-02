OLETUS_KAPASITEETTI = 5
OLETUS_KASVATUS = 5


class IntJoukko:
    _kapasiteetti: int
    _kasvatuskoko: int

    _alkioiden_lkm: int
    _lista: list[int]

    # tämä metodi on ainoa tapa luoda listoja
    def _alusta_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        if kapasiteetti is None:
            self._kapasiteetti = OLETUS_KAPASITEETTI
        elif not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Virheellinen kapasiteetti")
        else:
            self._kapasiteetti = kapasiteetti

        if kasvatuskoko is None:
            self._kasvatuskoko = OLETUS_KASVATUS
        elif not isinstance(kasvatuskoko, int) or kasvatuskoko < 0:
            raise Exception("Virheellinen kasvatuskoko")
        else:
            self._kasvatuskoko = kasvatuskoko

        self._lista = self._alusta_lista(self._kapasiteetti)
        self._alkioiden_lkm = 0

    def _kopioi_elementteja(self, a, b, maara: int | None):
        if maara is None:
            maara = len(a)
        for i in range(0, maara):
            b[i] = a[i]
    def _uudelleenallokoi(self):
        # ei mahdu enempää, luodaan uusi säilytyspaikka luvuille
        if self._alkioiden_lkm % len(self._lista) == 0:
            kopio = self._lista
            self._kopioi_elementteja(self._lista, kopio, None)
            self._lista = self._alusta_lista(self._alkioiden_lkm + self._kasvatuskoko)
            self._kopioi_elementteja(kopio, self._lista, None)

    def kuuluu(self, alkio):
        return alkio in self._lista

    def lisaa(self, n):
        if self.kuuluu(n):
            return False
        self._lista[self._alkioiden_lkm] = n
        self._alkioiden_lkm = self._alkioiden_lkm + 1

        self._uudelleenallokoi()
        return True

    def poista(self, n):
        if not self.kuuluu(n):
            return False
        self._lista.remove(n)
        self._alkioiden_lkm = self._alkioiden_lkm - 1
        return True

    def mahtavuus(self):
        return self._alkioiden_lkm

    def to_int_list(self):
        taulu = self._alusta_lista(self._alkioiden_lkm)

        self._kopioi_elementteja(self._lista, taulu, len(taulu))

        return taulu

    @staticmethod
    def yhdiste(a, b):
        yhdiste = IntJoukko()

        for i in a.to_int_list():
            yhdiste.lisaa(i)
        for i in b.to_int_list():
            yhdiste.lisaa(i)

        return yhdiste

    @staticmethod
    def leikkaus(a, b):
        leikkaus = IntJoukko()

        for i in a.to_int_list():
            if b.kuuluu(i):
                leikkaus.lisaa(i)

        return leikkaus

    @staticmethod
    def erotus(a, b):
        erotus = IntJoukko()

        for i in a.to_int_list():
            erotus.lisaa(i)
        for i in b.to_int_list():
            erotus.poista(i)

        return erotus

    def __str__(self):
        if self._alkioiden_lkm == 0:
            return "{}"
        elif self._alkioiden_lkm == 1:
            return "{" + str(self._lista[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self._alkioiden_lkm - 1):
                tuotos = tuotos + str(self._lista[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self._lista[self._alkioiden_lkm - 1])
            tuotos = tuotos + "}"
            return tuotos
