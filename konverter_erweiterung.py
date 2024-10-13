dezimalzahlen = [10, 15, 255, 1024, 2048, 12648430]

def konvertierte_zahlen(dezimalzahlen):
    binär_liste = []
    hex_liste = []
    for zahl in dezimalzahlen:
        binär_liste.append(bin(zahl))
        hex_liste.append(hex(zahl))
        return binär_liste, hex_liste
    
binär_liste, hex_liste = konvertierte_zahlen(dezimalzahlen)

print("Dezimalzahlen:", dezimalzahlen)
print("Binärwerte:", binär_liste)
print("Hexwerte:", hex_liste)