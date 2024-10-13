class Student:
    def __init__(self, name, martikelnummer, noten):
        self.name = name
        self.martikelnummer = martikelnummer
        self.noten = noten

    def konvertiere_martikelnummer(self):
        binär = bin(self.martikelnummer)
        hexadezimal = hex(self.martikelnummer)
        return binär, hexadezimal
    
student1 = Student("Alice", 101, {"Mathematik": 1.7, "Informatik": 1.3, "Physik": 2.0})
student2 = Student("Bob", 202, {"Mathematik": 2.3, "Informatik": 2.7, "Physik": 1.9})
student3 = Student("Charlie", 303, {"Mathematik": 3.0, "Informatik": 2.1, "Physik": 2.5})


studenten = {
    101: student1,
    202: student2,
    303: student3
}

def student_ausgeben(martikelnummer):
    print("")
    if martikelnummer in studenten:
        student = studenten[martikelnummer]
        binär, hexadezimal = student.konvertiere_martikelnummer()
        print(f"Student: {student.name}")
        print("Note:")
        for fach, note in student.noten.items():
            print(f"{fach}: {note}")
        print(f"Martikelnummer: {student.martikelnummer}")
        print(f"Binär: {binär}")
        print(f"Hexadezimal: {hexadezimal}")
    else:
        print(f"Student mir Martikelnummer {martikelnummer} nicht gefunden.")

student_ausgeben(101)
student_ausgeben(303)
