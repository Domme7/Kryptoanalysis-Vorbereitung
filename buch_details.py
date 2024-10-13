bücher = {
    "Python lernen leicht gemacht": {
        "Autor": "Max Mustermann",
        "Jahr": 2021,
        "ISBN": "123-456-789"
    },
    "Cybersecuriy Basics": {
        "Autor": "Anna Bauer",
        "Jahr": 2020,
        "ISBN": "987-654-321"
    },
    "KI und Zukunft": {
        "Autor": "Tom Tester",
        "Jahr": 2022,
        "ISBN": "456-123-789"
    }
}

for titel in bücher:
    print(titel)

def print_info(titel):
    print(bücher[titel])

print_info("KI und Zukunft")