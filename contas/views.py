from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import TransacaoForm
from .models import Transacao
import datetime


def home(request):
    template_name = 'contas/home.html'
    context = {}
    context['transacoes'] = ['t1', 't2', 't3']
    context['now'] = datetime.datetime.now()
    return render(request, template_name, context)


def listagem(request):
    template_name = 'contas/listagem.html'
    context = {}
    context['transacoes'] = Transacao.objects.all()
    return render(request, template_name, context)


def nova_transacao(request):
    template_name = 'contas/form.html'
    context = {}
    form = TransacaoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_listagem')
    context['form'] = form
    return render(request, template_name, context)


def update(request, pk):
    template_name = 'contas/form.html'
    context = {}
    transacao = Transacao.objects.get(pk=pk)
    form = TransacaoForm(request.POST or None, instance=transacao)

    if form.is_valid():
        form.save()
        return redirect('url_listagem')
    context['form'] = form
    context['transacao'] = transacao
    return render(request, template_name, context)


def delete(request, pk):
    transacao = Transacao.objects.get(pk=pk)
    transacao.delete()
    return redirect('url_listagem')
