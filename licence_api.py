from flask import Flask, request, jsonify

app = Flask(__name__)

# Simule une base de données des clés
licences = {
    "ABC123": True,
    "XYZ789": False,
    "theolapute": True
}

@app.route('/')
def home():
    return "API de licence active ✅"

@app.route('/check_key', methods=['POST'])
def check_key():
    data = request.get_json()
    key = data.get("key", "")
    
    if key in licences:
        if licences[key]:
            return jsonify({"status": "valid"}), 200
        else:
            return jsonify({"status": "disabled"}), 403
    return jsonify({"status": "not_found"}), 404

if __name__ == '__main__':
    app.run()
