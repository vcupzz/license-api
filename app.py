<<<<<<< HEAD
from flask import Flask, request, jsonify, render_template, redirect
import sqlite3
import os

app = Flask(__name__)

DB_PATH = "licences.db"

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

# === API de vérification de clé ===
@app.route('/check_key', methods=['POST'])
def check_key():
    data = request.get_json()
    key = data.get('key', '').strip().upper()

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT active FROM licences WHERE key = ?", (key,))
    result = cur.fetchone()
    conn.close()

    if result is None:
        return jsonify({"error": "Clé non trouvée"}), 404
    elif result["active"] == 1:
        return jsonify({"success": True}), 200
    else:
        return jsonify({"error": "Clé désactivée"}), 403

# === Interface d'administration ===
@app.route('/', methods=['GET', 'POST'])
def admin():
    conn = get_db_connection()
    cur = conn.cursor()

    if request.method == 'POST':
        new_key = request.form.get('key', '').strip().upper()
        if new_key:
            cur.execute("INSERT INTO licences (key, active) VALUES (?, 1)", (new_key,))
            conn.commit()

    cur.execute("SELECT * FROM licences")
    keys = cur.fetchall()
    conn.close()
    return render_template("admin.html", keys=keys)

# === Activer/Désactiver une clé ===
@app.route('/toggle/<key>')
def toggle_key(key):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT active FROM licences WHERE key = ?", (key,))
    result = cur.fetchone()
    if result:
        new_status = 0 if result['active'] == 1 else 1
        cur.execute("UPDATE licences SET active = ? WHERE key = ?", (new_status, key))
        conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    app.run()
=======
from flask import Flask, request, jsonify, render_template, redirect
import sqlite3
import os

app = Flask(__name__)

DB_PATH = "licences.db"

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

# === API de vérification de clé ===
@app.route('/check_key', methods=['POST'])
def check_key():
    data = request.get_json()
    key = data.get('key', '').strip().upper()

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT active FROM licences WHERE key = ?", (key,))
    result = cur.fetchone()
    conn.close()

    if result is None:
        return jsonify({"error": "Clé non trouvée"}), 404
    elif result["active"] == 1:
        return jsonify({"success": True}), 200
    else:
        return jsonify({"error": "Clé désactivée"}), 403

# === Interface d'administration ===
@app.route('/', methods=['GET', 'POST'])
def admin():
    conn = get_db_connection()
    cur = conn.cursor()

    if request.method == 'POST':
        new_key = request.form.get('key', '').strip().upper()
        if new_key:
            cur.execute("INSERT INTO licences (key, active) VALUES (?, 1)", (new_key,))
            conn.commit()

    cur.execute("SELECT * FROM licences")
    keys = cur.fetchall()
    conn.close()
    return render_template("admin.html", keys=keys)

# === Activer/Désactiver une clé ===
@app.route('/toggle/<key>')
def toggle_key(key):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT active FROM licences WHERE key = ?", (key,))
    result = cur.fetchone()
    if result:
        new_status = 0 if result['active'] == 1 else 1
        cur.execute("UPDATE licences SET active = ? WHERE key = ?", (new_status, key))
        conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    app.run()
>>>>>>> b362b34f59eb4c4e330d4b98df5afdc7de3aa74d
