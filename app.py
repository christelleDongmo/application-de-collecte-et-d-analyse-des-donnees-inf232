from flask import Flask, render_template, request
import sqlite3
import os

app = Flask(__name__)
DB_NAME = 'etudiants.db'

# Fonction pour initialiser la base de données
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS donnees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sexe TEXT,
            sommeil REAL,
            travail REAL,
            stress INTEGER,
            assiduite REAL,
            moyenne REAL
        )
    ''')
    conn.commit()
    conn.close()

# Initialisation au démarrage
init_db()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Connexion à la base
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        # Insertion des données
        cursor.execute('''
            INSERT INTO donnees (sexe, sommeil, travail, stress, assiduite, moyenne)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (
            request.form.get('sexe'),
            float(request.form.get('sommeil')),
            float(request.form.get('travail')),
            int(request.form.get('stress')),
            float(request.form.get('assiduite')),
            float(request.form.get('moyenne'))
        ))
        
        conn.commit()
        conn.close()
        return "Données enregistrées avec succès dans la base SQLite !"
    
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)