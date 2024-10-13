class Auto:
    def __init__(self, marke, modell, baujahr, preis):
        self.marke = marke
        self.modell = modell
        self.baujahr = baujahr
        self.preis = preis 

    def preis_senken(self):
        aktuelles_jahr = 2024
        alter = aktuelles_jahr - self.baujahr
        if alter > 5:
            self.preis *= 0.9 
            print(f"Das Auto {self.marke} {self.modell} ist gebraucht. Neuer Preis: {self.preis}€.")
        else:
            print(f"Das Auto {self.marke} {self.modell} ist neu. Preis bleibt: {self.preis}€.")

auto1 = Auto("BMW", "X5", 2016, 30000)
auto2 = Auto("Audi", "A3", 2021, 25000)

print(f"{auto1.preis}€.")
print(f"{auto2.preis}€.")

auto1.preis_senken()
auto2.preis_senken()