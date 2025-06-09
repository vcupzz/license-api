from flask import Flask, request, jsonify, render_template, redirect
import sqlite3

app = Flask(__name__)
DB_PATH = "licences.db"

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/', methods=['GET', 'POST'])
def admin():
    conn = get_db_connection()
    if request.method == 'POST':
        key = request.form.get('key', '').strip().upper()
        if key:
            conn.execute("INSERT OR IGNORE INTO licences (key, active) VALUES (?, 1)", (key,))
            conn.commit()
    rows = conn.execute("SELECT key, active FROM licences").fetchall()
    conn.close()
    return render_template('admin.html', keys=rows)

@app.route('/toggle/<key>')
def toggle(key):
    conn = get_db_connection()
    row = conn.execute("SELECT active FROM licences WHERE key=?", (key,)).fetchone()
    if row:
        new = 0 if row['active'] == 1 else 1
        conn.execute("UPDATE licences SET active=? WHERE key=?", (new, key))
        conn.commit()
    conn.close()
    return redirect('/')

@app.route('/check_key', methods=['POST'])
def check_key():
    data = request.get_json() or {}
    key = data.get('key', '').strip().upper()
    conn = get_db_connection()
    row = conn.execute("SELECT active FROM licences WHERE key=?", (key,)).fetchone()
    conn.close()
    if row and row['active'] == 1:
        return jsonify(status="valid"), 200
    return jsonify(status="invalid", error="Clé invalide ou désactivée"), 401

if __name__ == '__main__':
    app.run()

