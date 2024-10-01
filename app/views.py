from app import app
from flask import render_template,url_for


# sobre o sistema 
@app.route('/')
def index():
    return render_template('index.html')

# login
@app.route('/login/')
def login():
    return render_template('login.html')

# ocorrencias

@app.route('/ocorrencias/')
def ocorrencia():
    return render_template('ocorrencias.html')

# cadastro
@app.route('/cadastros/')
def cadastro():
    return render_template('cadastro.html')
