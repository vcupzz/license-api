<<<<<<< HEAD
from flask import Flask, render_template_string, request, redirect
import sqlite3

sqlite3.connect("C:/Users/Louis/Desktop/licence_api/licences.db")

app = Flask(__name__)

# HTML minimal avec formulaire
HTML = '''
<!doctype html>
<title>Admin Clés de Licence</title>
<h1>Gestion des Clés</h1>
<form method="post" action="/add">
    <input name="key" placeholder="Nouvelle clé" required>
    <button type="submit">Ajouter</button>
</form>
<table border=1 cellpadding=5>
<tr><th>Clé</th><th>Statut</th><th>Actions</th></tr>
{% for key, active in keys %}
<tr>
  <td>{{ key }}</td>
  <td>{{ 'Active' if active else 'Désactivée' }}</td>
  <td>
    <a href="/toggle/{{ key }}">{{ 'Désactiver' if active else 'Activer' }}</a>
    <a href="/delete/{{ key }}" onclick="return confirm('Supprimer cette clé ?');">Supprimer</a>
  </td>
</tr>
{% endfor %}
</table>
'''

DB = "licences.db"

def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS licences (
        key TEXT PRIMARY KEY,
        active INTEGER
    )""")
    conn.commit()
    conn.close()

@app.route("/")
def index():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("SELECT key, active FROM licences")
    keys = c.fetchall()
    conn.close()
    return render_template_string(HTML, keys=keys)

@app.route("/add", methods=["POST"])
def add():
    key = request.form.get("key")
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("INSERT OR IGNORE INTO licences (key, active) VALUES (?, 1)", (key,))
    conn.commit()
    conn.close()
    return redirect("/")

@app.route("/toggle/<key>")
def toggle(key):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("UPDATE licences SET active = 1 - active WHERE key = ?", (key,))
    conn.commit()
    conn.close()
    return redirect("/")

@app.route("/delete/<key>")
def delete(key):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("DELETE FROM licences WHERE key = ?", (key,))
    conn.commit()
    conn.close()
    return redirect("/")

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
=======
from flask import Flask, render_template_string, request, redirect
import sqlite3

sqlite3.connect("C:/Users/Louis/Desktop/licence_api/licences.db")

app = Flask(__name__)

# HTML minimal avec formulaire
HTML = '''
<!doctype html>
<title>Admin Clés de Licence</title>
<h1>Gestion des Clés</h1>
<form method="post" action="/add">
    <input name="key" placeholder="Nouvelle clé" required>
    <button type="submit">Ajouter</button>
</form>
<table border=1 cellpadding=5>
<tr><th>Clé</th><th>Statut</th><th>Actions</th></tr>
{% for key, active in keys %}
<tr>
  <td>{{ key }}</td>
  <td>{{ 'Active' if active else 'Désactivée' }}</td>
  <td>
    <a href="/toggle/{{ key }}">{{ 'Désactiver' if active else 'Activer' }}</a>
    <a href="/delete/{{ key }}" onclick="return confirm('Supprimer cette clé ?');">Supprimer</a>
  </td>
</tr>
{% endfor %}
</table>
'''

DB = "licences.db"

def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS licences (
        key TEXT PRIMARY KEY,
        active INTEGER
    )""")
    conn.commit()
    conn.close()

@app.route("/")
def index():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("SELECT key, active FROM licences")
    keys = c.fetchall()
    conn.close()
    return render_template_string(HTML, keys=keys)

@app.route("/add", methods=["POST"])
def add():
    key = request.form.get("key")
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("INSERT OR IGNORE INTO licences (key, active) VALUES (?, 1)", (key,))
    conn.commit()
    conn.close()
    return redirect("/")

@app.route("/toggle/<key>")
def toggle(key):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("UPDATE licences SET active = 1 - active WHERE key = ?", (key,))
    conn.commit()
    conn.close()
    return redirect("/")

@app.route("/delete/<key>")
def delete(key):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("DELETE FROM licences WHERE key = ?", (key,))
    conn.commit()
    conn.close()
    return redirect("/")

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
>>>>>>> b362b34f59eb4c4e330d4b98df5afdc7de3aa74d
