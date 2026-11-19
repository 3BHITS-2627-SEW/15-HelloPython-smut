from mein_paket.meineKlasse import MeineKlasse

# Fortsetzung in der Datei
def main(einParameter : str = "nix", einZweiterParameter : str = "anix") -> None:  #Man kann hinter einen DEFAULT parameter, Keine DEFAULT Parameter mehr machen. Also nach dem ersten Parameter muss er einen default wert haben
    print(" ein Python CheatSheet!")

    meineliste : list = ["eins","zwei","drei","viele"]

    print("Mein Parameter: ", einParameter)
    print(f"Mein Parameter 2: {einZweiterParameter}")

    #Werte an liste anfügen
    meineliste.append("mehr")
    print("Append an liste: ",meineliste)

    #1. Objet anlegen
    meinObjekt = MeineKlasse()
    #2. mit Print ausgeben
    print(meinObjekt)


    #gib liste aus:
    print(*meineliste, sep=" - ")
    # * entpackt die liste
    # und fügt diese 1:1 als parameter in den funktionsaufruf ein

    print("Das vierte Element: ", meineliste[3], sep="\n")

    #die liste umdrehen
    neuelist = meineliste.copy()
    neuelist.reverse()

    print("Die Liste umgekehrt: ",neuelist)

    meineliste[3] = "vier"
    print(meineliste)

    # wie viele Elemente hat die liste
    print(f"In der Liste sind {len(meineliste)} Elemente")

    print(f"wir nehmen das element {neuelist.pop()} raus")
    print("verkehrte liste: ", neuelist)

    for einListenEintrag in meineliste:
        print("Ein Eintag in der Liste", einListenEintrag, sep=": ")

    # klassische for schleife
    for i in range(10):
        print(f"{i}, ")

    for i in range(1,10+1, 2):
        print(f" {i},")

#rufe hauptfunktion
if __name__ == "__main__":
    main() #verwende default parameter
    main("schon etwas")
    main(einZweiterParameter="November")
    main(einZweiterParameter="November", einParameter="is no None")

