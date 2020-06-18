from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

from .models import Card, Janre

def card_page(request):
  cards = Card.objects.all()
  return render(request, template_name='cards/card_page.html', context={'cards': cards})

def card_detail(request, slug):
  card = Card.objects.get(slug__iexact=slug)
  return render(request, template_name='cards/card_detail.html', context={'card': card})

def janres_page(request):
  janres = Janre.objects.all()
  return render(request, template_name='cards/janres_page.html', context={'janres': janres})

def janre_detail(request, slug):
  janre = Janre.objects.get(slug__iexact=slug)
  return render(request, template_name='cards/janre_detail.html', context={'janre': janre})

def about(request):
  return render(request, template_name='cards/about.html')