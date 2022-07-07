from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model

from myshop.models.categories import Categories


User = get_user_model()


class Products(models.Model):
    name = models.CharField(max_length=255, verbose_name="mahsulotning nomi")
    slug = models.SlugField(max_length=250, unique=True, null=True, blank=True)
    description=models.TextField(null=True, blank=False,verbose_name="mahsulot haqida qisqacha")
    price = models.FloatField(verbose_name="mahsulotning narxi")
    discount = models.PositiveIntegerField(
        verbose_name="Chegirma", default=0, blank=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name="category")
    image_450_200 = models.ImageField(
        verbose_name='450x200', blank=True, default="banner_1.jpg")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    @property
    def imageURL(self) -> str:
        """This function for to fix images url"""
        try:
            url = self.image_450_200.url
        except:
            url = ""
        return url
    
    @property
    def isLiked(self) -> bool:
        """This function for to return isLiked bool"""
        return Likes.objects.only('liked').get(products_id=self.id)
    
    
    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name


class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    products = models.ForeignKey('Products', on_delete=models.DO_NOTHING)
    liked = models.BooleanField(default=False, null=True, blank=True)
    
    def isTrue(self):
        self.liked = True
        self.save()
    
    @property
    def isLiked(self):
        return self.liked