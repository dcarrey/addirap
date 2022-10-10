#!/usr/bin/python

#=============================
#== Serveur Flask
#=============================
__auteur__ = "Alix Boc"
__date__   = "2022"

from flask import Flask, render_template, request, jsonify, session
import addirap

# Setup Flask app.
app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/newGrid', methods=['POST'])
def newGrid():
    operation    = request.form.get('operation')
    nbOperations = int(request.form.get('nbOperations'))
    duree        = int(request.form.get('duree'))
    operations   = addirap.generate(nbOperations=nbOperations,operation=operation)
    return render_template("index.html",
                           operations=operations,
                           operation=operation,
                           symbole=addirap.getSymbole(operation),
                           duree=duree)

@app.route('/getDocx')
def downloadRandomGrid():
    operations = addirap.generate(50)
    return render_template("index.html",operations=operations)

@app.route('/')
def default ():
    nbOperations = 50
    operation    = "addition"
    duree        = 120
    operations   = addirap.generate(nbOperations=nbOperations,operation=operation)
    return render_template("index.html",
                           operation=operation,
                           operations=operations,
                           duree=duree)

@app.route('/<path:path>')
def all_files(path):
    return app.send_static_file(path)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')
