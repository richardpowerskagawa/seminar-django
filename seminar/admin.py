from django.contrib import admin

# Register your models here.
from .models import Seminar, Review

admin.site.register(Seminar)
admin.site.register(Review)