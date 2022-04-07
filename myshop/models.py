from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Categories(models.Model):
    name = models.CharField(max_length=30, null=True, blank=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True, blank=False, verbose_name="name")
    about = models.TextField()
    image = models.ImageField(verbose_name="600x600", null=True, blank=True)
    image2 = models.ImageField(verbose_name='828x828', null=True, blank=True)
    image3 = models.ImageField(verbose_name='427x427', null=True, blank=True)
    image4 = models.ImageField(verbose_name='1410x690', null=True, blank=True)
    image5 = models.ImageField(verbose_name='450x200', null=True, blank=True)
    mini_body = models.CharField(max_length=30, null=True, blank=False, verbose_name="qisqacha ma'lumot")
    discount_info = models.CharField(max_length=30, null=True, blank=False, verbose_name="chegirma haqida ma'lumot")
    price = models.FloatField()
    likes = models.IntegerField(blank=False, default=0)
    watches = models.IntegerField(blank=False, default=0)
    reviews = models.ManyToManyField('Reviews', blank=True)
    
    @property
    def imageURL(self): 
        """This function for to fix images url"""
        try:
            url = self.image4.url
        except:
            url = ""
        return url

    def __str__(self):
        return self.name
    

class Reviews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return str(self.user)


class SliderImage(models.Model):
    title = models.CharField(max_length=20, null=True, blank=False)
    body = models.CharField(max_length=40, null=True, blank=False)
    mini_body = models.CharField(max_length=50, null=True, blank=False)
    image = models.ImageField(verbose_name="1920x500 rasm")
    
    def __str__(self):
        return self.title
    
    @property
    def imageURL(self): 
        """This function for to fix images url"""
        try:
            url = self.image.url
        except:
            url = ""
        return url
    