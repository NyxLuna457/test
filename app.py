from flask import Flask
import mariadb
import sys
db_config = {        
        'user' : 'root',
        'password' : 'tssr14*',
        'host' : 'localhost',      # ou l'IP de l'hôte si ce n'est pas sur la même machine
        'port' : 3306,            # port par défaut de MariaDB
        'database' : 'NYXDB'    # optionnel, selon ta configuration
     }

try:
    # Remplace les valeurs ci-dessous par tes identifiants
    conn = mariadb.connect(**db_config)
    conn.ping()
    print("yes")
    conn.close()
except mariadb.Error as err:
    print(f"Erreur lors de la connexion à MariaDB : {err}")
    


app = Flask(__name__)

@app.route('/')
def afficher_personnes():
    try:
        conn = mariadb.connect(**db_config)
        cur = conn.cursor()
        cur.execute("SELECT id, nom, prenom, age, Job FROM personnes;")
        personnes = cur.fetchall()
        conn.close()
    except mariadb.Error as e:
        return f"<h1>Erreur de connexion à la base de données :</h1><pre>{e}</pre>"

    # Template HTML simple
    html = '''
    <h1>Liste des personnes</h1>
    <table border="1">
        <tr>
            <th>ID</th><th>Nom</th><th>Prénom</th><th>Âge</th><th>Job</th>
        </tr>
        {% for p in personnes %}
        <tr>
            <td>{{ p[0] }}</td>
            <td>{{ p[1] }}</td>
            <td>{{ p[2] }}</td>
            <td>{{ p[3] }}</td>
            <td>{{ p[4] }}</td>
        </tr>
        {% endfor %}
    </table>
    '''
    return render_template_string(html, personnes=personnes)

@app.route('/')
def home ():
    with open( 'templates/index.html', 'r') as file:
        return file.read()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)