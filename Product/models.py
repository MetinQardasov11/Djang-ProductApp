from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField(unique=True, blank=True, null=False, db_index=True, editable=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

class Product(models.Model):
    name = models.CharField(max_length=300)
    price = models.IntegerField()
    description = RichTextField()
    image = models.ImageField(upload_to='products')
    is_active = models.BooleanField(default=False)
    is_bestseller = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, blank=True, null=False, db_index=True, editable=False)
    categories = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)
        
