from django.contrib import admin

from .models import Category, Comment, Genre, Review, Title, User


@admin.register(User)
class User(admin.ModelAdmin):
    exclude = ('user_permissions',)


admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Title)
admin.site.register(Review)
admin.site.register(Comment)
