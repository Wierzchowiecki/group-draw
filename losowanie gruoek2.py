import os
import random
import csv


# Funkcja do losowania grup
def losuj_grupy(single, pary):
    grupy = []
    for _ in range(5):
        grupa_singli = random.sample(single, 3)
        single = [osoba for osoba in single if osoba not in grupa_singli]

        grupa = grupa_singli + random.sample(pary, min(len(pary), 2))
        pary = [para for para in pary if para not in grupa[-2:]]

        grupy.append(grupa)

    return grupy


# Lista osób
lista = ["Adam i Wanda ", "Ola D.", "Stasiu K", " Marta i Antoni K.. ", "Marcin", "Michal", "Ola_P.", " Wojciech i Judyta Sch. ", " Lukasz i Patrycja ", " Stasiu i Ania ", " Franek i Judyta Sz. ", "Gabriela", "Grzegorz",
         "Krzychu", " Paweł i Maria Po. ", " Jacek i Ida ", "Teresa", " Marek i Malgorzata ", "Piotr", "Maria_Gn", "Zuzanna",
         "Marta_P.", "Antoni", "Magda W."]
random.shuffle(lista)

# Podziel listę na dwie grupy: krótsze i dłuższe niż 8 znaków
krotsza_niz_8 = []
dluzsza_niz_8 = []

for l in lista:
    if len(l) <= 8:
        krotsza_niz_8.append(l)
    else:
        dluzsza_niz_8.append(l)

# Utwórz katalog, jeśli nie istnieje
sciezka_do_katalogu = 'C:\\MojeDokumenty'
os.makedirs(sciezka_do_katalogu, exist_ok=True)

# Losuj i zapisz grupy do pliku CSV
grupy = losuj_grupy(krotsza_niz_8, dluzsza_niz_8)

with open(os.path.join(sciezka_do_katalogu, 'wylosowane_grupy.csv'), 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)

    for i, grupa in enumerate(grupy, start=1):
        # Konwertuj elementy grupy na stringi
        grupa_do_zapisu = [str(element) for element in [f"Grupa {i}"] + grupa]
        csvwriter.writerow(grupa_do_zapisu)

    print("Plik 'wylosowane_grupy.csv' został zapisany pomyślnie.")
print("Grupki losowe", "wylosowane_grupy")
print("Liczba Małrzeństw:", len(dluzsza_niz_8))
print("Liczba Singli:", len(krotsza_niz_8))


