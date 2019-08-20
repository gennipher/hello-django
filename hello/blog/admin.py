from django.contrib import admin
from .models import Post

admin.site.register(Post) #Para tornar o modelo visível na página de administração
