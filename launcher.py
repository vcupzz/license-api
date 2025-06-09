import requests
import subprocess

API_URL = "https://license-api-oo2j.onrender.com/check_key"  # Remplace par ton URL Render si nécessaire
EXE_PATH = r"C:\Users\Louis\AppData\Local\Temp\LGHub\dfa98s4dfg9SD4GSD84Fa.exe"

def check_license_key(key):
    try:
        response = requests.post(API_URL, json={"key": key})
        if response.status_code == 200:
            return True
        else:
            print(f"⛔ Clé refusée : {response.json().get('error')}")
            return False
    except Exception as e:
        print(f"❌ Erreur de connexion : {e}")
        return False

def main():
    key = input("🔐 Entrez votre clé d'activation : ").strip().upper()
    if check_license_key(key):
        print("✅ Clé valide. Lancement de l'application...")
        subprocess.run(EXE_PATH)
    else:
        print("⛔ Accès refusé.")

    input("Appuyez sur Entrée pour quitter...")

if __name__ == "__main__":
    main()
