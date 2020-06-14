from django.contrib import admin

from .models import Card, Janre

class CardAdmin(admin.ModelAdmin): 
  list_display = ('id', 'title', 'slug', 'header')
  list_display_links = ('id', 'title')
  search_fields = ('header', )

class JanreAdmin(admin.ModelAdmin):
  list_display = ('id', 'title')
  list_display_links = ('id', 'title')
  search_fields = ('title', )

admin.site.register(Card, CardAdmin)
admin.site.register(Janre, JanreAdmin)
