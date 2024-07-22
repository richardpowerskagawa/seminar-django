from django.contrib import admin

# Register your models here.
from .models import Seminar, Review, Video

admin.site.register(Seminar)
admin.site.register(Review)
admin.site.register(Video)