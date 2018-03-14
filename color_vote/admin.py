from django.contrib import admin
from .models import Word, Vote

# test pass1234
admin.site.register(Word)
admin.site.register(Vote)