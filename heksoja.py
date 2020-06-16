def muotoile_heksaluvuksi(muutettava_luku, bittien_maara):
    heksa = hex(muutettava_luku).lstrip('0x')
    heksa = heksa.zfill((bittien_maara - muutettava_luku.bit_length())//4 + len(heksa))
    return heksa


try:
    luku = int(input('Anna kokonaisluku: '))
    bitit = int(input('Anna heksaluvun pituus (bittien lukumäärä): '))
except ValueError as e:
    print('Kokonaisluku kiitos')
else:
    print(muotoile_heksaluvuksi(luku, bitit))
