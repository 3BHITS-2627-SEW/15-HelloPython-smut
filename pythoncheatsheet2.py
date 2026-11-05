import numpy 

#bennene ein paket um
import numpy as npy

from mein_paket.meineKlasse import *

def main():
    number = numpy.sqrt(4)
    print("Wurzel aus 4: ", number)

    number2 = npy.sqrt(16)
    print("Wurzel aus 16: ", number2)

    meinObjekt = Klass()
    print("Name vom Objekt: ", meinObjekt.name)
    pass


if __name__ == "__main__":
    main()
    