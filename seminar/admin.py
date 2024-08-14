from django.contrib import admin

# Register your models here.
from .models import Seminar, Review, Video

# admin.site.register(Seminar)
# admin.site.register(Review)
# admin.site.register(Video)


# @admin.register(Seminar)
# class SeminarAdmin(admin.ModelAdmin):
#     list_display = ('title', 'category')
#     search_fields = ('title', 'category')
#     # Add any other configurations you need here

# @admin.register(Video)
# class VideoAdmin(admin.ModelAdmin):
#     list_display = ('title', 'seminar', 'upload_date')
#     search_fields = ('title', 'seminar__title')
#     list_filter = ('seminar',)
#     # Add any other configurations you need here


class VideoInline(admin.TabularInline):
    model = Video
    extra = 1

class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1
    readonly_fields = ('user', 'created_at')  # Adjust as necessary

@admin.register(Seminar)
class SeminarAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    search_fields = ('title', 'category')
    inlines = [VideoInline, ReviewInline]

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'seminar', 'upload_date')
    search_fields = ('title', 'seminar__title')
    list_filter = ('seminar',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'seminar', 'user', 'rate', 'created_at')
    search_fields = ('title', 'seminar__title', 'user__username')
    list_filter = ('seminar', 'user', 'rate')