import sqlite3

# Verbindung zur Datenbank herstellen (falls nicht vorhanden, wird sie erstellt)
conn = sqlite3.connect('meine_datenbank.db')

# Ein Cursor-Objekt erstellen, um SQL-Befehle auszuführen
cursor = conn.cursor()

# Neue Daten einfügen
cursor.execute("INSERT INTO Schueler (vorname, nachname, geburtsdatum) VALUES (?, ?, ?)", ('Test', 'Baum', '2002-01-01'))
conn.commit()
