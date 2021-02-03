from flask import render_template, jsonify, request

from . import app


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ajax", methods=["POST"])
def ajax():
    user_text = request.form["userText"]
    # print("La requête:" user_text)
    return jsonify('Pas de réponse pour le moment.')

""""
1. Récupérer la question depuis la requête HTTP
2. appeler la fonction answer ci-dessus, en lui envoyant la question du visiteur en argument, et en récupérant le dictionnaire retourné
3. Transforme le dictionnaire retourné en réponse HTTP json et retourne cette réponse.
"""