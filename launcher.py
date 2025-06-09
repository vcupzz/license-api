import requests
import subprocess

# URL de ton API Render
API_URL = "https://license-api-csqu.onrender.com/check_key"

# Chemin vers ton .exe à lancer si la clé est valide
EXE_PATH = r"C:\Users\Louis\AppData\Local\Temp\LGHub\dfa98s4dfg9SD4GSD84Fa.exe"

def main():
    key = input("🔑 Entrez votre clé de licence : ").strip()

    try:
        # Envoi de la clé à l'API
        response = requests.post(API_URL, json={"key": key}, timeout=5)

        # DEBUG : Affiche la réponse brute
        print("🔎 Réponse brute:", response.text)

        # Vérifie que la réponse est bien du JSON
        data = response.json()

        # Analyse de la réponse
        if response.status_code == 200 and data.get("status") == "valid":
            print("✅ Clé valide ! Lancement de l'application...")
            subprocess.Popen(EXE_PATH, shell=True)
        else:
            print("⛔ Accès refusé. Clé invalide ou désactivée.")

    except Exception as e:
        print(f"🚫 Erreur : {e}")

if __name__ == "__main__":
    main()
