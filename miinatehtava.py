TULOSTUKSET = {
    "ulkona": "Antamasi ruutu on kentän ulkopuolella.",
    "nurkassa": "Antamasi ruutu on kentän nurkassa.",
    "laidalla": "Antamasi ruutu on kentän laidalla.",
    "keskellä": "Antamasi ruutu on keskikentällä."
}

def sijainti_kentalla(ruudun_x, ruudun_y, kentan_leveys, kentan_korkeus):
    avain = ''
    if ruudun_x < 0 or ruudun_y < 0 or ruudun_x >= kentan_leveys or ruudun_y >= kentan_korkeus:
        avain = 'ulkona'
    elif (ruudun_x == 0 and ruudun_y == 0) or (ruudun_x == 0 and ruudun_y == kentan_korkeus-1) or (ruudun_x == kentan_leveys-1 and ruudun_y == 0) or (ruudun_x == kentan_leveys-1 and ruudun_y == kentan_korkeus-1):
        avain = 'nurkassa'
    elif ruudun_x == 1 or ruudun_y == 1 or ruudun_x == kentan_leveys-1 or ruudun_y == kentan_korkeus-1:
        avain = 'laidalla'
    else:
        avain = 'keskellä'

    return avain


def tulosta_sijainti(avain):
    print(TULOSTUKSET[avain])


leveys = int(input('Anna kentän leveys: '))
korkeus = int(input('Anna kentän korkeus: '))

if leveys <= 0 or korkeus <= 0:
    print('Noin pienelle kentälle ei mahdu ainuttakaan ruutua!')
else:
    x = int(input('Anna x-koordinaatti: '))
    y = int(input('Anna y-koordinaatti: '))
    sijainti = sijainti_kentalla(x, y, leveys, korkeus)
    tulosta_sijainti(sijainti)
    