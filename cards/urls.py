from django.urls import path

from .views import card_page, card_detail, janres_page, janre_detail, about

urlpatterns = [
    path('', card_page, name='card_page_url'),
    path('card/<str:slug>/', card_detail, name='card_detail_url'),
    path('janres/', janres_page, name='janres_page_url'),
    path('janre/<str:slug>/', janre_detail, name='janre_detail_url'),
    path('about/', about, name='about_url')
]
