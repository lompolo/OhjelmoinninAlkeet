"""
Määrittelee aasigotchin käyttöliittymän toiminnot.
"""
import aasimaaritelmat as am


def pyyda_syote(aasidata):
    """
    Näyttää käyttäjälle aasin tilaa vastaavat mahdolliset syötteet ja kysyy uutta
    syötettä kunnes käyttäjä antaa laillisen syötteen. Saatu syöte palautetaan.
    """
    if aasidata["ELÄKE"]:
        print('Valinnat: q, a')
    else:
        print('Valinnat: q, r, k, t')

    while(True):
        try:
            valinta = input('Anna seuraava valinta: ')
            if valinta == 'q':
                return am.LOPETA
            elif aasidata["ELÄKE"]:
                if valinta == 'a':
                    return am.ALUSTA
            else:
                if valinta == 'r':
                    return am.RUOKI
                elif valinta == 'k':
                    return am.KUTITA
                elif valinta == 't':
                    return am.TYOSKENTELE
            print('Virheellinen syöte!')
        except EOFError as e:
            print(end="")

def nayta_tila(aasidata):
    """
    Tulostaa aasin tilan.
    """
    print('Aasi on {} vuotta vanha ja rahaa on {} mk.'.format(aasidata["IKÄ"], aasidata["RAHA"]))
    print('Kylläisyys: {}'.format(aasidata["KYLLÄISYYS"]))
    print('Onnellisuus: {}'.format(aasidata["ONNELLISUUS"]))
    print('Jaksaminen: {}'.format(aasidata["JAKSAMINEN"]))
    if aasidata["ELÄKE"]:
        print('Aasi on jäänyt eläkkeelle.')
