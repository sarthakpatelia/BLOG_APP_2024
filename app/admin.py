from django.contrib import admin

from app.models import *

# Register your models here.

admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(Tag)
admin.site.register(Blog)