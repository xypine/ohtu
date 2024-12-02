from enum import Enum
from tkinter import ttk, constants, StringVar

from sovelluslogiikka import Sovelluslogiikka


class Komento(Enum):
    SUMMA = 1
    EROTUS = 2
    NOLLAUS = 3
    KUMOA = 4

class Summa:
    def __init__(self, sovelluslogiikka: Sovelluslogiikka, hae_syote):
        self._sovelluslogiikka = sovelluslogiikka
        self._hae_syote = hae_syote

    def suorita(self):
        arvo = self._hae_syote()
        self._sovelluslogiikka.plus(arvo)


class Erotus:
    def __init__(self, sovelluslogiikka: Sovelluslogiikka, hae_syote):
        self._sovelluslogiikka = sovelluslogiikka
        self._hae_syote = hae_syote

    def suorita(self):
        arvo = self._hae_syote()
        self._sovelluslogiikka.miinus(arvo)


class Nollaus:
    def __init__(self, sovelluslogiikka: Sovelluslogiikka, hae_syote):
        self._sovelluslogiikka = sovelluslogiikka
        self._hae_syote = hae_syote

    def suorita(self):
        self._sovelluslogiikka.nollaa()


class Kumoa:
    def __init__(self, sovelluslogiikka: Sovelluslogiikka, hae_aikaisempi_arvo):
        self._sovelluslogiikka = sovelluslogiikka
        self._hae_aikaisempi_arvo = hae_aikaisempi_arvo

    def suorita(self):
        aikaisempi = self._hae_aikaisempi_arvo()
        if aikaisempi is not None:
            self._sovelluslogiikka.aseta_arvo(aikaisempi)

class Kayttoliittyma:
    def __init__(self, sovelluslogiikka, root):
        self._sovelluslogiikka = sovelluslogiikka
        self._root = root
        self._komennot = {
            Komento.SUMMA: Summa(sovelluslogiikka, self._hae_syote),
            Komento.EROTUS: Erotus(sovelluslogiikka, self._hae_syote),
            Komento.NOLLAUS: Nollaus(sovelluslogiikka, self._hae_syote),
            Komento.KUMOA: Kumoa(sovelluslogiikka, self._hae_aikaisempi_arvo),
        }
        self._historia = []

    def _hae_syote(self):
        try:
            arvo = int(self._syote_kentta.get())
            return arvo
        except Exception:
            pass

    def _hae_aikaisempi_arvo(self):
        if len(self._historia) > 0:
            return self._historia.pop()
        return None

    def kaynnista(self):
        self._arvo_var = StringVar()
        self._arvo_var.set(self._sovelluslogiikka.arvo())
        self._syote_kentta = ttk.Entry(master=self._root)

        tulos_teksti = ttk.Label(textvariable=self._arvo_var)

        summa_painike = ttk.Button(
            master=self._root,
            text="Summa",
            command=lambda: self._suorita_komento(Komento.SUMMA)
        )

        erotus_painike = ttk.Button(
            master=self._root,
            text="Erotus",
            command=lambda: self._suorita_komento(Komento.EROTUS)
        )

        self._nollaus_painike = ttk.Button(
            master=self._root,
            text="Nollaus",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.NOLLAUS)
        )

        self._kumoa_painike = ttk.Button(
            master=self._root,
            text="Kumoa",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.KUMOA)
        )

        tulos_teksti.grid(columnspan=4)
        self._syote_kentta.grid(columnspan=4, sticky=(constants.E, constants.W))
        summa_painike.grid(row=2, column=0)
        erotus_painike.grid(row=2, column=1)
        self._nollaus_painike.grid(row=2, column=2)
        self._kumoa_painike.grid(row=2, column=3)

    def _suorita_komento(self, komento):
        if komento != Komento.KUMOA:
            self._historia.append(self._sovelluslogiikka.arvo())

        komento_olio = self._komennot[komento]
        komento_olio.suorita()

        self._kumoa_painike["state"] = constants.NORMAL

        if self._sovelluslogiikka.arvo() == 0:
            self._nollaus_painike["state"] = constants.DISABLED
        else:
            self._nollaus_painike["state"] = constants.NORMAL
        
        if len(self._historia) > 0:
            self._kumoa_painike["state"] = constants.NORMAL
        else:
            self._kumoa_painike["state"] = constants.DISABLED

        self._syote_kentta.delete(0, constants.END)
        self._arvo_var.set(self._sovelluslogiikka.arvo())
