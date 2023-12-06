import sqlite3

# Verbindung zur Datenbank herstellen (falls nicht vorhanden, wird sie erstellt)
conn = sqlite3.connect('meine_datenbank.db')

# Ein Cursor-Objekt erstellen, um SQL-Befehle auszuführen
cursor = conn.cursor()

# Alle Schüler abfragen
cursor.execute("SELECT * FROM Schueler")
schueler = cursor.fetchall()

for schueler in schueler:
    print(schueler)