from django.db import models
from mongoengine import *

class User(Document):
    username = StringField(required=True)
    password = StringField(required=True)
    deviceID = StringField(required=False)


class ClienteFis(Document):
    nome = StringField(required=True)
    CPF = StringField(required=True)
    endereco = StringField(required=True)
    email = StringField(required=True)
    telefone = StringField(required=True)
    codigo = StringField(required=True)
    user = ObjectIdField(required=True)

class ClienteJur(Document):
    razao_social = StringField(required=True)
    CNPJ = StringField(required=True)
    endereco = StringField(required=True)
    email = StringField(required=True)
    telefone = StringField(required=True)
    user = ObjectIdField(required=True)

class Produto(Document):
    temperatura = StringField(required=True)
    umidade = StringField(required=True)
    ruido = StringField(required=True)
    luminosidade = StringField(required=True)
    link = StringField(required=True)
    link_foto = StringField(required=True)
    user = ObjectIdField(required=True)
