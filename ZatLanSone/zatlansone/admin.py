from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Episode)
admin.site.register(Content)
admin.site.register(Story)