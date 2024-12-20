from enum import Enum
from kps import KiviPaperiSakset
from tekoaly import Tekoaly
from tekoaly_parannettu import TekoalyParannettu


class KPSVariantti(Enum):
    PVP = 0
    TKOALY = 1
    TKOALY_PARANNETTU = 2
def luo_pelivariantti(var: KPSVariantti) -> KiviPaperiSakset:
    match var:
        case KPSVariantti.PVP:
            return KPSPelaajaVsPelaaja()
        case KPSVariantti.TKOALY:
            return KPSTekoaly()
        case KPSVariantti.TKOALY_PARANNETTU:
            return KPSParempiTekoaly()

class KPSPelaajaVsPelaaja(KiviPaperiSakset):
    def _toisen_siirto(self, ensimmaisen_siirto):
        return input("Toisen pelaajan siirto: ")

class KPSTekoaly(KiviPaperiSakset):
    def _toisen_siirto(self, ensimmaisen_siirto):
        siirto = self._tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {siirto}")
        self._tekoaly.aseta_siirto(ensimmaisen_siirto)
        return siirto

    def pelaa(self):
        self._tekoaly = Tekoaly()
        super().pelaa()

class KPSParempiTekoaly(KiviPaperiSakset):
    def _toisen_siirto(self, ensimmaisen_siirto):
        siirto = self._tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {siirto}")
        self._tekoaly.aseta_siirto(ensimmaisen_siirto)
        return siirto

    def pelaa(self):
        self._tekoaly = TekoalyParannettu(10)
        super().pelaa()


