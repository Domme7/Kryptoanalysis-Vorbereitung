class Auto:
    def __init__(self, marke, modell, baujahr):
        self.marke = marke
        self.modell = modell
        self.baujahr = baujahr

    def details_ausgeben(self):
        print(f"Auto: {self.marke} {self.modell}, Baujahr: {self.baujahr}")

mein_auto = Auto("Toyota", "Corolla", 2020)

mein_auto.details_ausgeben()