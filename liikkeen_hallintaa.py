import math

def muunna_xy_koordinaateiksi(kulma, sade):
    return int(round(sade * math.cos(kulma), 0)), int(round(sade * math.sin(kulma), 0))


def kysy_liike(parm_dict):
    print('Hahmo on sijainnissa ({}, {})'.format(parm_dict['x'], parm_dict['y']))
    parm_dict['suunta'] = int(input('Anna liikkumissuunta asteina: '))
    parm_dict['nopeus'] = int(input('Anna liikenopeus: '))



def paivita_sijainti(param_dict):
    x, y = muunna_xy_koordinaateiksi(math.radians(param_dict['suunta']), param_dict['nopeus'])
    param_dict['x'] += x
    param_dict['y'] += y
    print('Uusi sijainti: ({}, {})'.format(param_dict['x'], param_dict['y']))


hahmo_1 = {
    "x": 0,
    "y": 0,
    "suunta": 0,
    "nopeus": 0
}

hahmo_2 = {
    "x": 50,
    "y": 50,
    "suunta": 0,
    "nopeus": 0
}

vuoro = 1
while vuoro < 3:
    print("Pelaaja {} vuoro".format(vuoro))
    kysy_liike(hahmo_1) if vuoro == 1 else kysy_liike(hahmo_2)
    paivita_sijainti(hahmo_1) if vuoro == 1 else paivita_sijainti(hahmo_2)
    vuoro += 1
