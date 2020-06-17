def pyyda_syote(pyynto, virhe):
    while True:
        try:
            luku = int(input(pyynto))
        except ValueError:
            print(virhe)
        else:
            return luku


luku = pyyda_syote(
    "Anna kokonaisluku: ",
    "Et antanut kokonaislukua"
)
print("Annoit kokonaisluvun {}! Nohevaa toimintaa!".format(luku))
hemulit = pyyda_syote(
    "Montako hemulia mahtuu muumitaloon? ",
    "Tämä ei ollut kelvollinen hemulien lukumäärä!"
)
print("Muumitaloon mahtuu {} hemulia".format(hemulit))
