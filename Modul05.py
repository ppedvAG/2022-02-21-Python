# Klassen

class Tisch():
    x = 100

    def __init__(self, anzBeine: int, ablageflaeche: float, material: str):
        # Konvention ist es den ersten Parameter self zu nennen
        self.beine = anzBeine
        self.ablageflaeche = ablageflaeche
        self.material = material

    def __str__(self) -> str:
        return f"Ein Tisch aus {self.material} mit {self.beine} Beinen und einer Ablagefläche von " \
               f"{self.ablageflaeche} cm^2"

    def talk(self, text: str) -> None:
        print(text)

    @staticmethod
    def xSquared():
        return Tisch.x * Tisch.x





class Fahrzeug():

    def __init__(self, baujahr: int, reifen: int, hubraum: int, marke: str):
        self._baujahr = baujahr
        self._reifen = reifen
        self._hubraum = hubraum
        self._marke = marke

    @property # wird zum getter
    def baujahr(self) -> int:
        return self._baujahr


    @baujahr.setter
    def baujahr(self, newBaujahr: int) -> None:
        if newBaujahr < 1900:
            print("Gab da noch keine Autos")
        else:
            self._baujahr = newBaujahr

    @baujahr.deleter
    def baujahr(self):
        print("Löschen nicht möglich")
        self._baujahr = None

    def __str__(self):
        return f"Baujahr: {self.baujahr} |  Reifen: {self._reifen} | Hubraum: {self._hubraum} | Marke: {self._marke}"





class Pkw(Fahrzeug):
    def __init__(self, baujahr, hubraum, marke, modell: str):
        super().__init__(baujahr, 4, hubraum, marke)
        self.modell = modell
        self.motor = False

    def __str__(self):
        return super().__str__() + f" | Modell: {self.modell} | Motor: {self.motor}"



class Lkw(Fahrzeug, Tisch):

    def __init__(self, baujahr, hubraum, marke):
        """

        :param baujahr:
        :param hubraum:
        :param marke:
        """
        # Fahrzeug.__init__()
        # Tisch.__init__()
        super().__init__()
        super(Fahrzeug, self).__init__()


def main():
    schreibtisch = Tisch(2, 100, "Eiche")
    schreibtisch.talk("Hallo Welt")
    schreibtisch.schubladen = 3  # Fügt das dynamische Attribut Schublade hinzu
    schreibtisch.beine = 24

    del schreibtisch.schubladen
    # del schreibtisch.x # Darf nicht gelsöcht werden, da Klassenfield
    # del schreibtisch.beine Geht, da es sich um eine Instanz Variable handelt
    print(type(schreibtisch))
    print(schreibtisch)
    print(isinstance(schreibtisch, object))  # Prüft ob es eine Instanz der Klasse ist, bei object immer True, da es
    # der Ursprung ist

    print(issubclass(Tisch, object))
    print(issubclass(Tisch, str))

    testAuto = Fahrzeug(1955, 4, 250, "Ford")
    testAuto._reifen = 12
    print(testAuto)

    audi = Pkw(2000, 300, "Audi", "A4")
    print(audi)

    print(Tisch.x)
    print(Tisch.xSquared())

    print(__name__)


if __name__ == "__main__":
    main()
