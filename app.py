from flask import Flask, request, render_template, redirect, url_for
import sqlite3
from salt import salt_password
import base64
app = Flask(__name__)

# Route om het formulier weer te geven
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

# Route om formuliergegevens te verwerken
@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    password = request.form['password']
    salt = salt_password(password)
    hashed_password = salt_password(password + salt)


    # Maak verbinding met de SQLite database
    conn = sqlite3.connect('wachtwoord.db', timeout=10, check_same_thread=False)

    cursor = conn.cursor()

    # Voeg de nieuwe gebruiker toe aan de database zonder hashing
    cursor.execute('INSERT INTO users (username, salt, password) VALUES (?, ?, ?)', (username, salt, hashed_password))

    # Sla de wijzigingen op en sluit de verbinding
    conn.commit()
    conn.close()

    # Leid de gebruiker terug naar de home-pagina of geef een succesbericht weer
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, port=5004)
