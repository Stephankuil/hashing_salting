import sqlite3

# Maak verbinding met de database (dit maakt de database aan als deze nog niet bestaat)
conn = sqlite3.connect('wachtwoord.db')

# Maak een cursor-object
cursor = conn.cursor()

# Maak een tabel 'users' aan als deze nog niet bestaat
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
)
''')

# Wijzigingen opslaan
conn.commit()

# Sluit de verbinding
conn.close()
