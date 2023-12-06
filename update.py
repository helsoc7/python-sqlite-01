import sqlite3

# Verbindung zur Datenbank herstellen (falls nicht vorhanden, wird sie erstellt)
conn = sqlite3.connect('meine_datenbank.db')

# Ein Cursor-Objekt erstellen, um SQL-Befehle auszuführen
cursor = conn.cursor()

# Vorname eines Schülers aktualisieren
cursor.execute("UPDATE Schueler SET vorname = ? WHERE nachname = ?", ('Maximilian', 'Mustermann'))
conn.commit()
