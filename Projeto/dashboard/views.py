from django.shortcuts import render,redirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth ,messages
from login.models import PerfilAluno
from login.models import Pessoa
from login.models import exercicios
import random
import login.views

from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

from django.contrib import messages

def dashboard(request):

    if request.user.is_authenticated:
        profiles = PerfilAluno.objects.get(user=request.user.id)
        
        if profiles.usuario == "1":
            exercicio = exercicios.objects.all()
            dados={
            'exercicios' : exercicio,
        }
            return render(request,'dashboard.html',dados)




        else:
            alunos = PerfilAluno.objects.filter(usuario=1)
            o = 0
            for aluno in alunos:
                o+=1
            dados = {
                'ativos' : o,
    
            }
            return render(request,'teacher_dashboard.html',dados)
    else:
        return redirect('login')


def propor_exercicio(request):
    
    if request.user.is_authenticated:
        profiles = PerfilAluno.objects.get(user=request.user.id)
        if profiles.usuario == "1":

            return render(request,'dashboard.html')
        else:
            if request.method == 'POST':
                nome = request.POST['nome']
                enunciado = request.POST['enunciado']
                resposta = request.POST['resposta']
                try:
                    fotos = request.FILES['foto']
                except :
                    fotos = '/media/static/imagens/user.png'

                questao = exercicios.objects.create(nome=nome, enunciado=enunciado, resposta=resposta,imagem=fotos)  
                questao.save() 




                return render(request,'propor.html')
            else:
                return render(request,'propor.html')
    else:
        return redirect('login')