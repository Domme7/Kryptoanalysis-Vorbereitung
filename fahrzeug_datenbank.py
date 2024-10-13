class Fahrzeug:
    def __init__(self, marke, modell, baujahr, preis):
        self.marke = marke 
        self.modell = modell
        self.baujahr = baujahr
        self.preis = preis 

    def konventiere_preis(self):
        binär_preis = bin(self.preis)
        hex_preis = hex(self.preis)
        return binär_preis, hex_preis
    
fahrzeug1 = Fahrzeug("BMW", "X5", 2016, 30000) 
fahrzeug2 = Fahrzeug("Audi", "A3", 2021, 25000)
fahrzeug3 = Fahrzeug("Tesla", "Model S", 2022, 80000)

fahrzeuge = {
    "BMW X5": fahrzeug1,
    "Audi A3": fahrzeug2,
    "Tesla Model S": fahrzeug3
}

def fahrzeug_preis_ausgeben(fahrzeug_name):
    if fahrzeug_name in fahrzeuge:
        fahrzeug = fahrzeuge[fahrzeug_name]
        binär_preis, hex_preis = fahrzeug.konventiere_preis()
        print("")
        print(f"Fahrzeug: {fahrzeug.marke} {fahrzeug.modell}")
        print(f"Dezimaler Preis: {fahrzeug.preis}€")
        print(f"Binärer Preis: {binär_preis}")
        print(f"Hexadezimaler Preis: {hex_preis}")
    else:
        print(f"Fahrzeug {fahrzeug_name} nicht in der Datenbank gefunden.")

fahrzeug_preis_ausgeben("BMW X5")
fahrzeug_preis_ausgeben("Tesla Model S")