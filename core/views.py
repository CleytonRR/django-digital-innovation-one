from django.shortcuts import render
from core.models import Evento
from django.contrib.auth.decorators import login_required
# Create your views here.

def login_user(request):
    return render(request, 'login.html')

@login_required(login_url='/login/')
def lista_eventos(request):
    evento = Evento.objects.all()
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)
