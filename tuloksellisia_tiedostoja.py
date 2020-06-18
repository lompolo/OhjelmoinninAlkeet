def nayta_tulokset(tiedosto):
    tulokset = []
    try:
        with open(tiedosto) as data:
            for rivi in data.readlines():
                pelaaja1, pelaaja2, tulos1, tulos2 = rivi.split(",")
                tulokset.append([pelaaja1.strip(), pelaaja2.strip(), int(tulos1), int(tulos2)])
    except IOError:
        print('Ongelmia tiedoston avaamisessa')
    except ValueError:
        print('Vääränlainen rivi')
    else:
        for rivi in tulokset:
            print('{} {} - {} {}'.format(rivi[0], rivi[2], rivi[3], rivi[1]))


nayta_tulokset("hemulicup.csv")
