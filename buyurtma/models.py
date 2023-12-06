from django.db import models
from asosiy.models import Mahsulot
from userapp.models import Profil

class Tanlangan(models.Model):
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)

class Savat(models.Model):
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    total_sum = models.PositiveIntegerField(default=0)
    holat = models.CharField(max_length=15, blank=True)

class SavatItem(models.Model):
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    savat = models.ForeignKey(Savat, on_delete=models.CASCADE)
    miqdor = models.PositiveSmallIntegerField(default=1)
    summa = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        chegirma = (self.mahsulot.narx * self.mahsulot.chegirma)//100
        narx = self.mahsulot.narx - chegirma
        self.summa = narx
        super(SavatItem, self).save(*args, **kwargs)
