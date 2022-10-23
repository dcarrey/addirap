#!/usr/bin/python

#=============================
#== Serveur Flask
#=============================
__auteur__ = "Alix Boc"
__date__   = "2022"

from flask import Flask, render_template, request, jsonify, session
import addirap, random, uuid

# Setup Flask app.
app = Flask(__name__)
app.secret_key = 'secret22'

MAX_VALUE = {"addition":9,"soustraction":18}
@app.route('/newGrid', methods=['POST'])
def newGrid():
    if 'id' not in session.keys():
        session["id"] = uuid.uuid1()
    operation    = request.form.get('operation')
    nbOperations = int(request.form.get('nbOperations'))
    duree        = int(request.form.get('duree'))
    operations   = addirap.generate(nbOperations=nbOperations,operation=operation, maxValue=MAX_VALUE[operation])
    niveau       = "moyen"
    userId       = "alix"
    outputfile = "addirap-" + operation + "-" + niveau + "-" + str(session['id']) + ".docx"
    addirap.afficher("docx",niveau,operations,operation=operation,outputfile="static/grilles/"+outputfile)
    return render_template("index.html",
                           operations=operations,
                           operation=operation,
                           symbole=addirap.getSymbole(operation),
                           duree=duree,
                           outputfile=outputfile)

@app.route('/')
def default ():
    nbOperations = 50
    operation    = "addition"
    duree        = 120
    operations   = addirap.generate(nbOperations=nbOperations,operation=operation)
    return render_template("index.html",
                           operation=operation,
                           operations=operations,
                           duree=duree,
                           symbole=addirap.getSymbole(operation))

@app.route('/<path:path>')
def all_files(path):
    return app.send_static_file(path)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')
