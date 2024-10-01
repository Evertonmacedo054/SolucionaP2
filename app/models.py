
#Banco de dados - PostgreSQL

# Apenas um exemplo
from app import db
from datetime import datetime

# ser modificado

class Contato(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_envio = db.Column(db.DateTime, default = datetime.now)
    nome = db.Column(db.String, nullable= True)
    email = db.Column(db.String, nullable= True)
    assunto = db.Column(db.String, nullable= True)
    mensagens = db.Column(db.String, nullable= True)

# a ser modificado

class login():
    pass

# a ser modificado

class ocorrenica():
    pass