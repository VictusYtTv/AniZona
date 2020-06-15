from django.urls import path
from .views import card_page, card_detail

urlpatterns = [
    path('', card_page, name='card_page_url'),
    path('card/<str:slug>/', card_detail, name='card_detail_url'),
]
