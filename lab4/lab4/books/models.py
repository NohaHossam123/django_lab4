from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Books(models.Model):
    title = models.CharField(max_length=25)
    image = models.FileField(max_length=20)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

