from django.contrib import admin
from .models import Book, Borrow, Review

# Register your models here.
admin.site.register(Book)
admin.site.register(Borrow)
admin.site.register(Review)