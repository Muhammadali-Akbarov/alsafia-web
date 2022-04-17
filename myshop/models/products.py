from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model

from myshop.models.categories import Categories

User = get_user_model()


class Products(models.Model):
    name = models.CharField(max_length=255, verbose_name="mahsulotning nomi")
    slug = models.SlugField(max_length=250, unique=True, null=True, blank=True)
    price = models.FloatField(verbose_name="mahsulotning narxi")
    discount = models.PositiveIntegerField(
        verbose_name="Chegirma", default=0, blank=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    image_450_200 = models.ImageField(
        verbose_name='450x200', blank=True, default="default/banner-1.jpg")
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @property
    def imageURL(self):
        """This function for to fix images url"""
        try:
            url = self.image_450_200.url
        except:
            url = ""
        return url

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
