def kysy_salasana():
    while True:
        merkkijono = input("Kirjoita salasana: ")

        if len(merkkijono) >= 8:
            return merkkijono

        print("Salasanan tulee olla vähintään 8 merkkiä pitkä")


print(kysy_salasana())
