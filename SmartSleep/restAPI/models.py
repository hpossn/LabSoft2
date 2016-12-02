from django.db import models
from mongoengine import *
import datetime

class User(Document):
    username = StringField(required=True)
    password = StringField(required=True)
    deviceID = StringField(required=False)

class information(Document):
    deviceID = StringField(required=True)
    location = StringField(required=True)
    data = FloatField(required=True)
    dataType = StringField(required=True)
    dateTime = DateTimeField(default=datetime.datetime.now)

class ClienteFis(Document):
    nome = StringField(required=True)
    CPF = StringField(required=True)
    endereco = StringField(required=True)
    email = StringField(required=True)
    telefone = StringField(required=True)
    user = ObjectIdField(required=True)
    dateTime = DateTimeField(default=datetime.datetime.now)

class Produto(Document):
    temperatura = StringField(required=True)
    umidade = StringField(required=True)
    ruido = StringField(required=True)
    luminosidade = StringField(required=True)
    link = StringField(required=True)
    link_foto = StringField(required=True)
    user = ObjectIdField(required=True)
