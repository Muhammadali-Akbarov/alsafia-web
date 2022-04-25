from django.db import models


class Categories(models.Model):
    ALL = 0
    ENG_KOP_SOTILADIGAN=1
    TOP_10=2
    YANGILAR=3
    KUN_TAKLIFLARI=4
    SIZ_UCHUN_TAVFSIYA=5
    BOSHQALAR=6
    ENG_MASHHUR_MAHSULOTLAR=7
    
    name = models.CharField(max_length=30, null=True, blank=False)
    
    def __str__(self):
        return str(f"ID-{self.id} {self.name}")
    
        