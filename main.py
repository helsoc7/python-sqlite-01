import sqlite3

# Verbindung zur Datenbank herstellen (falls nicht vorhanden, wird sie erstellt)
conn = sqlite3.connect('meine_datenbank.db')

# Ein Cursor-Objekt erstellen, um SQL-Befehle auszuführen
cursor = conn.cursor()

# Beispiel: Tabelle erstellen (Schüler)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Schueler (
        id INTEGER PRIMARY KEY,
        vorname TEXT,
        nachname TEXT,
        geburtsdatum DATE
    )
''')

# Änderungen speichern und Verbindung schließen
# Neue Daten einfügen
# Alle Schüler abfragen
cursor.execute("SELECT * FROM Schueler")
schueler = cursor.fetchall()

for schueler in schueler:
    print(schueler)

conn.close()
