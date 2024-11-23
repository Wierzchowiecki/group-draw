from flask import Flask, render_template, request, redirect, url_for, send_file
import random
import os
import csv

app = Flask(__name__)

# Prosta baza użytkowników
users = {"admin": "wspolnota"}


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
lista = ["Adam i Wanda", "Ola D.", "Stasiu K", "Marta i Antoni K..", "Marcin", "Michal", "Ola P.", "Wojciech i Judyta Sch.", "Lukasz i Patrycja", "Stasiu i Ania", "Franek i Judyta Sz.", "Gabriela", "Grzegorz",
         "Krzychu", "Pawel i Maria Po.", "Jacek i Ida", "Teresa", "Marek i Malgorzata", "Piotr", "Maria_Gn", "Zuzanna",
         "Marta_P.", "Antoni", "Magda W."]
random.shuffle(lista)

@app.route('/')
def home():
    return render_template('home.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            return redirect(url_for('losowanie'))
        return "Nieprawidłowe dane logowania!"
    return render_template('login.html')


@app.route('/losowanie')
def losowanie():
    krotsza_niz_8 = [l for l in lista if len(l) <= 8]
    dluzsza_niz_8 = [l for l in lista if len(l) > 8]
    grupy = losuj_grupy(krotsza_niz_8, dluzsza_niz_8)

    # Zapis grup do pliku CSV
    sciezka_do_pliku = 'wylosowane_grupy.csv'
    with open(sciezka_do_pliku, 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        for i, grupa in enumerate(grupy, start=1):
            csvwriter.writerow([f"Grupa {i}"] + grupa)

    return send_file(sciezka_do_pliku, as_attachment=True)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

