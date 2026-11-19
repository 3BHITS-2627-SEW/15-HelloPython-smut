class MeineKlasse:
    # Konstruktor
    def __init__(self):
        # self ist ein this pointer

        # name wir eine instanzvariable
        self.__name = "EineKlasse"
        # pass macht einfach nix
    def noNoneNovember(self): # self ist immer die eigene instanz
        # Hier kommt der Methoden Rumpf
        
        return("November!")


    def get_name(self) -> str:
        return self.__name

    def set_name(self, neuer_name : str) -> None:
        self.__name = neuer_name
        pass

    ## special-Methode
    ## magic-Methode
    ## dunner-Methode
    # __METHODE__(self):

    #überschreibe Methode __str__
    # enstpricht einer ToString() Methode in C++
    def __str__(self) -> str:
        return f"Eine Instanz der Klasse 'MeineKlasse' mit dem Namen {self.__name}"

    