import requests

key = input("🔑 Entrez votre clé de licence : ").strip()

try:
    response = requests.post(
        "https://license-api-csqu.onrender.com/check_key",
        json={"key": key},
        timeout=5
    )
    data = response.json()

    if response.status_code == 200 and data.get("status") == "valid":
        print("✅ Clé valide !")
        # Ici tu peux lancer ton .exe
    else:
        print("⛔ Accès refusé.")
except Exception as e:
    print(f"🚫 Erreur : {e}")
