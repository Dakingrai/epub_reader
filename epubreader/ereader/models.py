from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.urls import reverse

class Book(models.Model):
    name = models.CharField(max_length=200, null=False)
    author = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='static/images')
    description = models.TextField(null=True)
    category = models.ManyToManyField('Category',  blank=True)
    book = models.FileField(upload_to='static/books', null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Category(MPTTModel):
    name = models.CharField(max_length=200, null=False)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    def get_absolute_url(self):
        return reverse('library_list', args=[str(self.id)])

    def __str__(self):
        return self.name

