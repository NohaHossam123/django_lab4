from django.contrib import admin
from .models import Books
from .models import Author

admin.site.register(Books)
admin.site.register(Author)
# Register your models here.
