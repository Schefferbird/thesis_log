from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()

    def __str__(self):
        return self.name
    

class Log(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    body = models.TextField()
    author = models.ForeignKey('Author', related_name='logs', on_delete=models.PROTECT)

    def __str__(self):
        return self.title