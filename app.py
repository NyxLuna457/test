from flask import Flask

app = Flask(__name__)

@app.route('/')
def home ():
    with open( 'templates/index.html', 'r') as file:
        return file.read()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

import mariadb
import sys

try:
    # Remplace les valeurs ci-dessous par tes identifiants
    conn = mariadb.connect(
        user="root",
        password="tssr14*",
        host="localhost",      # ou l'IP de l'hôte si ce n'est pas sur la même machine
        port=3306,            # port par défaut de MariaDB
        database="NYXDB"    # optionnel, selon ta configuration
    )
    print("yes")
    conn.close()
except mariadb.Error as e:
    print(f"Erreur lors de la connexion à MariaDB : {e}")
    sys.exit(1)
