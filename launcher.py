import requests
import subprocess
import os

# === CONFIGURATION ===

# API Render en ligne (met ici l'URL complète de ton render.com si actif)
URL_API = "https://license-api-oo2j.onrender.com/check_key"  # ou https://mon-api.render.com/check_key

# Chemin de ton .exe
EXE_PATH = r"C:\Users\Louis\AppData\Local\Temp\LGHub\dfa98s4dfg9SD4GSD84Fa.exe"

# === FONCTIONS ===

def verifier_cle_en_ligne(cle):
    try:
        response = requests.post(URL_API, json={"key": cle})
        if response.status_code == 200:
            return True
        elif response.status_code == 403:
            print("❌ Clé désactivée.")
        elif response.status_code == 404:
            print("❌ Clé inexistante.")
        else:
            print(f"❌ Erreur inconnue (code {response.status_code})")
    except Exception as e:
        print(f"❌ Erreur de connexion à l'API :\n{e}")
    return False

def lancer_application():
    if os.path.exists(EXE_PATH):
        print("▶️ Lancement de l'application...")
        subprocess.Popen([EXE_PATH], shell=True)
    else:
        print("❌ Fichier .exe introuvable :", EXE_PATH)

# === PROGRAMME PRINCIPAL ===

def main():
    cle_utilisateur = input("🔐 Entrez votre clé d'activation : ").strip().upper()

    if verifier_cle_en_ligne(cle_utilisateur):
        print("✅ Clé valide.")
        lancer_application()
    else:
        print("⛔ Accès refusé.")

    input("\nAppuyez sur Entrée pour quitter...")  # Évite la fermeture immédiate si lancé par double-clic

if __name__ == "__main__":
    main()
