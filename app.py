import csv
from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

# Ta carte du bar de plage
# Vérifie que CHAQUE plat a bien sa ligne "image"
menu = {
    "Cocktails": [
        {
            "nom": "Mojito Royal",
            "prix": "12€",
            "description": "Menthe fraîche, citron vert, rhum ambré et champagne.",
            "image": "https://images.unsplash.com/photo-1551024709-8f23befc6f87?w=400"
        },
        {
            "nom": "Piña Colada",
            "prix": "10€",
            "description": "Ananas frais, crème de coco, rhum blanc.",
            "image": "https://assets.tmecosys.com/image/upload/t_web_rdp_recipe_584x480/img/recipe/ras/Assets/A9467000-4182-4A69-802E-6A36234604C1/Derivates/9cca3d9b-727b-4d23-b633-71dcd23125da.jpg"
        }
    ],
    "Tapas": [
        {
            "nom": "Planche de la mer",
            "prix": "18€",
            "description": "Calamars, crevettes grillées et tartinable de thon.",
            "image": "https://images.unsplash.com/photo-1541529086526-db283c563270?w=400"
        }
    ]
}


@app.route('/')
def home():
    return render_template('index.html', carte=menu)


@app.route('/reserver', methods=['GET', 'POST']) # Vérifie bien qu'il y a GET et POST
def reservation():
    if request.method == 'POST':
        nom = request.form.get('nom')
        nb_personnes = request.form.get('personnes')
        heure = request.form.get('heure')
        date_res = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Enregistrement dans le fichier Excel (CSV)
        with open('reservations.csv', mode='a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([date_res, nom, nb_personnes, heure])

        return render_template('confirmation.html', nom=nom)

    return render_template('reservation.html')


if __name__ == '__main__':
    app.run(debug=True)