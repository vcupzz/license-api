# fichier: licence_api.py
import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

# Initialisation (à exécuter une fois pour créer la table)
def init_db():
    conn = sqlite3.connect("licences.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS licences (key TEXT PRIMARY KEY, active INTEGER)")
    conn.commit()
    conn.close()

@app.route('/')
def home():
    return "API de licence avec base de données 🧠"

@app.route('/check_key', methods=['POST'])
def check_key():
    data = request.json
    key = data.get("key", "")
    
    conn = sqlite3.connect("licences.db")
    c = conn.cursor()
    c.execute("SELECT active FROM licences WHERE key=?", (key,))
    result = c.fetchone()
    conn.close()

    if result is None:
        return jsonify({"status": "not_found"}), 404
    elif result[0] == 1:
        return jsonify({"status": "valid"}), 200
    else:
        return jsonify({"status": "disabled"}), 403

if __name__ == '__main__':
    init_db()  # Création base à la première exécution
    app.run()
