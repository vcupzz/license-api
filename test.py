import requests

API_URL = "http://127.0.0.1:5000/check_key"
key = input("🔑 Clé à tester : ").strip().upper()

try:
    response = requests.post(API_URL, json={"key": key})
    print("Réponse :", response.json())
except Exception as e:
    print("Erreur :", e)

input("Appuyez sur Entrée pour quitter...")
