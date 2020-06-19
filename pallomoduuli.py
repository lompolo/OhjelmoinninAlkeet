import math

def laske_ala(sade):
    return 4 * math.pi * sade ** 2
    
def laske_tilavuus(sade):
    return 4 / 3 * math.pi * sade ** 3

def laske_sade(piiri):
    return piiri / (math.pi * 2)


if __name__ == "__main__":
    print("Tämä ohjelma laskee pallon tilavuuden ja pinta-alan, kun tiedetään pallon ympärysmitta")
    try:
        piiri = float(input("Anna pallon ympärysmitta: "))
    except ValueError:
        print("Syötteessä tulee olla pelkästään numeroarvo.")
    else:
        sade = laske_sade(piiri)
        ala = laske_ala(sade)
        tilavuus = laske_tilavuus(sade)
        print("Tilavuus:")
        print(round(tilavuus, 4))
        print("Pinta-ala:")
        print(round(ala, 4))
