from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

from .models import Card

def card_page(request):
  cards = Card.objects.all()
  return render(request, template_name='cards/card_page.html', context={'cards': cards})