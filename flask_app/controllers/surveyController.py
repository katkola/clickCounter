from flask_app import app
from flask import redirect, render_template, request, session

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    print(request.form)
    session['name'] = request.form['name']
    session['dojo'] = request.form['dojo']
    session['favLang'] = request.form['favLang']
    session['comment'] = request.form['comment']

    return render_template('results.html')

