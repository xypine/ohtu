from kps_variantit import KPSVariantti, luo_pelivariantti

def pelaa_variantti(variantti: str):
    match variantti:
        case v if v.endswith("a"):
            kpsvar = KPSVariantti.PVP
        case v if v.endswith("b"):
            kpsvar = KPSVariantti.TKOALY
        case v if v.endswith("c"):
            kpsvar = KPSVariantti.TKOALY_PARANNETTU
        case _:
            return False

    print(
        "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
    )
    peli = luo_pelivariantti(kpsvar)
    peli.pelaa()
    return True

def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
        )
        vastaus = input()
        if not pelaa_variantti(vastaus):
            break

if __name__ == "__main__":
    main()
