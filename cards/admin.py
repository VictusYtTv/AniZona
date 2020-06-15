from django.contrib import admin

from .models import Card, Janre

class CardAdmin(admin.ModelAdmin): 
  list_display = ('title', 'slug', 'header', 'rating', 'date_published', 'is_published', )
  list_display_links = ('title', )
  search_fields = ('header', 'janre', 'title', )

class JanreAdmin(admin.ModelAdmin):
  list_display = ('title', 'slug', )
  list_display_links = ('title', )
  search_fields = ('title', )

admin.site.register(Card, CardAdmin)
admin.site.register(Janre, JanreAdmin)
