import cmath
from math import pi, degrees


def laske_osoitinmuoto(tyyppi, arvo, taajuus=0):
    
    if tyyppi == 'l':
        z = 2*pi * taajuus * arvo * 1j
    elif tyyppi == 'c':
        z = 1 / (2* pi * taajuus * arvo * 1j)
    else:
        z = arvo

    pituus, kulma_rad = cmath.polar(z)
    return pituus, kulma_rad


komponentti_tyyppi = input('Anna komponentin tyyppi (R, L, C): ')
if komponentti_tyyppi.lower() in ('r', 'l', 'c'):
    komponentti_arvo = float(input('Anna komponentin arvo: '))
    komponentti_taajuus = 0

    if komponentti_tyyppi.lower() in ('l', 'c'):
        komponentti_taajuus = float(input('Anna komponentin taajuus: '))

    komponentti_pituus, komponentti_kulma = laske_osoitinmuoto(komponentti_tyyppi.lower(), komponentti_arvo, komponentti_taajuus)
    print('Komponentin impedanssi osoitinmuodossa: {} < {:.3f}°'.format(komponentti_pituus, degrees(komponentti_kulma)))
else:
    print('Sallittuja komponentteja ovat R, L ja C!')
