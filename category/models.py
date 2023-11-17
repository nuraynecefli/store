from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=80, unique=True)
    desc = models.TextField(blank=True)
    
    def __str__(self) -> str:
        return self.category_name