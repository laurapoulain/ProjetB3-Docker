from flask import Flask, jsonify
import mysql.connector
import os
from flask_cors import CORS 

# Creation de l'application Flask
app = Flask(__name__)
CORS(app)

# Fonction  pour se connecter à la base de données MySQL
# utilise les variables d'environnement définies dans le fichier docker-compose.yml
def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )   

# Route pour indiquer que l'API est disponible
@app.route("/status")
def status():
    try:
        conn = get_connection()
        conn.close()
        return jsonify('OK')
    except:
        return "ERREUR", 500


# Route qui affiche la liste des objets presents dans la base MySQL
@app.route("/items")
def items():
    # Connexion à la base
    conn = get_connection()
    cursor = conn.cursor()

     # Requête SQL
    cursor.execute("SELECT id, name FROM items;")

    # Récupération objets
    rows = cursor.fetchall()

    # Fermeture de la connexion
    cursor.close()
    conn.close()

    # Conversion en JSON
    return jsonify([{"id": r[0], "name": r[1]} for r in rows])


# Lancement serveur Flask
if __name__ == "__main__":
    # écoute sur toutes les IP du conteneur (pour Docker), sur le port 8000
    app.run(host="0.0.0.0", port=int(os.getenv("API_PORT", 8000)))
