def kysy_kaksi_lukua(merkkijono):
    """
    Pyytää käyttäjältä kaksi liukulukua välilyönnillä erotettuna. Syötettä kysytään
    kunnes käyttäjä antaa kaksi kelvollista liukulukua. Syötetyt luvut palautetaan
    liukulukuina.
    """
    while True:
        syote = input(merkkijono).split(" ")

        if len(syote) != 2:
            print("Anna kaksi lukua välilyönnillä erotettuna")
            continue

        try:
            x = float(syote[0])
            y = float(syote[1])
            break
        except ValueError:
            print("Anna kaksi lukua välilyönnillä erotettuna")

    return x, y


def etsi_indeksit(sarja, minimi, maximi):
    """
    Etsii annetusta numeerista dataa sisältävästä listasta alku- ja päätepisteet
    siten, että alueen arvot ovat annettujen minimi- ja maksimiarvojen välissä.
    Palauttaa näiden pisteiden indeksit.
    """
    try:
        min_index = next(k for k in reversed(range(len(sarja))) if sarja[k] < minimi) + 1
    except StopIteration:
        min_index = 0

    try:
        max_index = next(k for k in reversed(range(len(sarja))) if sarja[k] <= maximi) + 1
    except StopIteration:
        max_index = 0

    return min_index, max_index


def main():
    mittauspisteet = [
        10.000, 10.244, 10.429, 10.576, 10.589, 10.606, 10.714, 10.794, 10.879, 10.99,
        11.263, 11.448, 11.596, 11.836, 11.869, 11.936, 12.174, 12.182, 12.243, 12.282,
        12.285, 12.297, 12.363, 12.417, 12.629, 12.71, 12.816, 13.138, 13.153, 13.215,
        13.27, 13.32, 13.367, 13.368, 13.923, 13.97, 14.171, 14.204, 14.235, 14.382,
        14.481, 14.581, 14.588, 14.645, 14.7, 14.704, 14.711, 14.803, 14.936, 15.000
    ]
    mittausarvot = [
        30.4, 74.165, 118.615, 54.293, 174.187, 162.399, 25.643, 181.571, 151.84, 147.307,
        85.115, 81.337, 65.852, 127.676, 10.409, 131.279, 32.595, 89.49, 40.263, 32.712,
        114.974, 7.967, 131.166, 124.827, 172.936, 145.234, 156.433, 118.446, 2.253, 69.263,
        99.249, 23.344, 119.2, 169.069, 187.976, 113.63, 173.847, 193.978, 54.206, 60.27,
        199.026, 167.434, 138.631, 3.259, 23.886, 88.825, 49.804, 109.179, 62.388, 126.052
    ]

    i, j = kysy_kaksi_lukua("Anna kaksi mittauspistettä välilyönnillä erotettuna: ")

    alku, loppu = etsi_indeksit(mittauspisteet, i, j)
    print("Antamaasi väliä vastaavat mittaustulokset: ")
    print(mittausarvot[alku: loppu])


if __name__ == "__main__":
    main()