import sqlite3
import hashlib
import base64

def check_user_login(username, password):
    # Maak verbinding met de SQLite database
    conn = sqlite3.connect('wachtwoord.db', timeout=10, check_same_thread=False)
    cursor = conn.cursor()

    # Zoek de gebruiker op basis van de gebruikersnaam
    cursor.execute('SELECT salt, password FROM users WHERE username = ?', (username,))
    result = cursor.fetchone()

    # Sluit de databaseverbinding
    conn.close()

    # Als de gebruiker niet bestaat
    if result is None:
        return False, "Gebruiker bestaat niet."

    # Haal de opgeslagen salt en gehashte wachtwoord op
    stored_salt = result[0]
    stored_hashed_password = result[1]

    # Decodeer de opgeslagen salt
    salt = base64.b64decode(stored_salt)

    # Combineer de salt met het ingevoerde wachtwoord en hash deze (gebruik dezelfde hashmethode)
    hashed_input_password = hashlib.sha512(salt + password.encode('utf-8')).digest()

    # Encodeer het gehashte wachtwoord voor vergelijking
    hashed_input_password_encoded = base64.b64encode(hashed_input_password).decode('utf-8')

    # Vergelijk het ingevoerde gehashte wachtwoord met het opgeslagen wachtwoord
    if hashed_input_password_encoded == stored_hashed_password:
        return True, "Inloggen gelukt."
    else:
        return False, "Onjuist wachtwoord."

# Voorbeeld gebruik
username = "one"  # invoer van de gebruiker
password = "one"  # invoer van de gebruiker

login_success, message = check_user_login(username, password)
print(message)
