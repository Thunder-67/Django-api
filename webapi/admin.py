from django.contrib import admin
from .models import categories,meals,search
# Register your models here.
admin.site.register(categories)
admin.site.register(meals)
admin.site.register(search)