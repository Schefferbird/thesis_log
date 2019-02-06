from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Log(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='logimg', blank=True, null=True, height_field="height_field", width_field="width_field")
    height_field=models.IntegerField(default=0)
    width_field=models.IntegerField(default=0)
    author = models.ForeignKey('Author', related_name='logs', on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created"]