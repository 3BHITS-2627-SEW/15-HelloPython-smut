import numpy 

#bennene ein paket um
import numpy as npy

from mein_paket.meineKlasse import MeineKlasse

def main():
    number = numpy.sqrt(4)
    print("Wurzel aus 4: ", number)

    number2 = npy.sqrt(16)
    print("Wurzel aus 16: ", number2)

    meinObjekt = MeineKlasse()
    print("Name vom Objekt: ","Private") # IST PRIVATE:  meinObjekt.__name

    print("Welcher Monat ist aktuell?", meinObjekt.noNoneNovember())

    print("Der Name vom Objekt via Getter:", meinObjekt.get_name())

    meinObjekt.set_name("meinObjekt")

    print("Der Name vom Objekt via Getter:", meinObjekt.get_name())

    pass


if __name__ == "__main__":
    main()
    