from django.urls import path
from .views import card_page

urlpatterns = [
    path('', card_page, name='card_page_url')
]
