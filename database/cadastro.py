from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
    __tablename__="usuarios"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    telefone = db.Column(db.String(15))
    email = db.Column(db.String, unique=True)
    objetivo = db.Column(db.String)

    def __init__(self, nome, telefone, email, objetivo):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.objetivo = objetivo

    def __rep__(self):
        return f"{self.nome}:{self.id}"