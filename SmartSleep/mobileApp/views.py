from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import requests
from .models import *

@csrf_exempt
def login(request):
    if request.method == 'GET':
        return render(request, 'index.html', {})

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        r = requests.post("http://127.0.0.1:8000/restAPI/login", data={"username" : username, "password" : password})

        r = r.json()

        if r['result'] == "Login Okay":
            return redirect('/mobileApp/home?deviceID='+r['deviceID'])
        else:
            return redirect('/mobileApp/login')


@csrf_exempt
def home(request):
    if request.method == 'GET':

        temperaturas = get_temperaturas(request.GET['deviceID'])

        return render(request, 'mainPage.html', {'deviceID' : request.GET['deviceID']})

def get_temperaturas(deviceID):
    all_temps = requests.get("http://127.0.0.1:8000/restAPI/temperaturas?deviceID=" + deviceID)

    firsDay=[]
    secondDay=[]
    thirdDay=[]
    fourthDay=[]
    fifthDay=[]
    sixthDa=[]

 #####################Views para cadastro###################### -->

@csrf_exempt
def cadastroFis(request):

    if request.method == "GET":
        return render(request, 'cadastroFis.html', {})

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        nome = request.POST['nome']
        CPF = request.POST['cpf']
        endereco = request.POST['endereco']
        email = request.POST['email']
        telefone = request.POST['telefone']
        codigo = request.POST['codigo']

        #r = requests.post("http://127.0.0.1:8000/restAPI/cadastroFis", data={"username" : username, "password" : password, "nome" : nome, "CPF" : CPF, "enderco" : endereco, "email" : email, "telefone" : telefone, "codigo" : codigo})

        # cria um novo usuario
        usuario = User(username=username, password=password, deviceID=codigo)
        usuario.save()
        # cria um objeto clienteFis para o novo usuario
        clienteFis = ClienteFis(nome=nome, CPF=CPF, endereco=endereco, email=email, telefone=telefone, codigo=codigo, user=usuario.id)
        clienteFis.save()

        return HttpResponseRedirect('/mobileApp/login')







@csrf_exempt
def cadastroJur(request):

    if request.method == "GET":

        return render(request, 'cadastroJur.html', {})

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        razao_social = request.POST['razaosocial']
        CNPJ = request.POST['cnpj']
        endereco = request.POST['endereco']
        email = request.POST['email']
        telefone = request.POST['telefone']


        #r = requests.post("http://127.0.0.1:8000/restAPI/cadastroJur", data={"username" : username, "password" : password, "razao_social" : razao_social, "CNPJ" : CNPJ, "enderco" : endereco, "email" : email, "telefone" : telefone})
        usuario = User(username=username, password=password)
        usuario.save()
        # cria um objeto clienteJur para o novo usuario
        clienteJur = ClienteJur(razao_social=razao_social, CNPJ=CNPJ, endereco=endereco, email=email, telefone=telefone, user=usuario.id)
        clienteJur.save()


        return HttpResponseRedirect('/mobileApp/login')
 ########################################### -->


######################Views da mainpage de um usuario pessoa juridica##################### -->
@csrf_exempt
def mainpageJur(request):
    if request.method == "GET":

        return render(request, 'mainpageJur.html', {})

    if request.method == "POST":

        usuario  =request.POST['usuario']
        temperatura = request.POST['temperatura']
        umidade = request.POST['umidade']
        ruido = request.POST['ruido']
        luminosidade = request.POST['luminosidade']
        link = request.POST['link']
        link_foto = request.POST['linkfoto']




        #r = requests.post("http://127.0.0.1:8000/restAPI/mainpageJur", data={"temperatura" : temperatura, "umidade" : umidade, "ruido" : ruido, "luminosidade" : lumisidade, "link" : link, "link_foto" : link_foto})
        #busca o usuário
        user = User.objects(username = usuario)

        if len(user) == 0:
            print("oi")
        else:
            # cria um objeto produto para o novo usuario
            produto = Produto(temperatura=temperatura, umidade=umidade, ruido=ruido, luminosidade=luminosidade, link=link, link_foto=link_foto, user=user[0].id)
            produto.save()

        return render(request, 'mainpageJur.html', {})
