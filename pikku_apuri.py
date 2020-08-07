MUUNNOS_TAULU = {
    "Y": 10**24,
    "Z": 10**21,
    "E": 10**18,
    "P": 10**15,
    "T": 10**12,
    "G": 10**9,
    "M": 10**6,
    "k": 10**3,
    "h": 10**2,
    "da": 10**1,
    "d": 10**-1,
    "c": 10**-2,
    "m": 10**-3,
    "u": 10**-6,
    "n": 10**-9,
    "p": 10**-12,
    "f": 10**-15,
    "a": 10**-18,
    "z": 10**-21,
    "y": 10**-24
}


def muuta_kerrannaisyksikko(muunnettava_luku):
    """
    Muuttaa annetun luvun ja mahdollisen kerrannaisyksikön vastaavaksi liukuluvuksi.
    """
    tunnus = muunnettava_luku[-1:]
    luku = muunnettava_luku[:-1] 

    if tunnus in MUUNNOS_TAULU.keys():  
        if tunnus == "a":
            if muunnettava_luku[-2: -1] == "d":
                tunnus = "da"
                luku = muunnettava_luku[:-2]
        
        potenssi = MUUNNOS_TAULU[tunnus]
    else:
        luku = muunnettava_luku
        potenssi = 1
        
    try:
        numero = float(luku)
        muunnos = numero * potenssi
    except ValueError:
        muunnos = None
    
    return muunnos


def main():
    while True:
        arvo = input("Anna muutettava arvo: ")
        muunnos = muuta_kerrannaisyksikko(arvo)
        if muunnos:
            print(muunnos)
            break

        print("Arvo ei ole kelvollinen")


if __name__ == "__main__":
    main()