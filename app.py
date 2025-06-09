from flask import Flask, request, jsonify, render_template, redirect
import sqlite3

app = Flask(__name__)
DB_PATH = "licences.db"

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def admin_panel():
    conn = get_db_connection()
    keys = conn.execute('SELECT * FROM licences').fetchall()
    conn.close()
    return render_template('admin.html', keys=keys)

@app.route('/', methods=['POST'])
def add_key():
    key = request.form['key'].strip().upper()
    conn = get_db_connection()
    conn.execute('INSERT OR IGNORE INTO licences (key, active) VALUES (?, ?)', (key, 1))
    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/toggle/<key>')
def toggle_key(key):
    conn = get_db_connection()
    current = conn.execute('SELECT active FROM licences WHERE key = ?', (key,)).fetchone()
    if current:
        new_status = 0 if current['active'] == 1 else 1
        conn.execute('UPDATE licences SET active = ? WHERE key = ?', (new_status, key))
        conn.commit()
    conn.close()
    return redirect('/')

@app.route('/check_key', methods=['POST'])
def check_key():
    data = request.get_json()
    key = data.get('key', '').strip().upper()

    conn = get_db_connection()
    result = conn.execute('SELECT active FROM licences WHERE key = ?', (key,)).fetchone()
    conn.close()

    if result and result['active'] == 1:
        return jsonify({"status": "valid"}), 200
    return jsonify({"status": "invalid", "error": "Clé invalide ou désactivée"}), 401

if __name__ == '__main__':
    app.run(debug=True)
