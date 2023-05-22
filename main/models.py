from django.db import models
from datetime import date


class طفل(models.Model):
    الاسم = models.CharField(max_length=100)
    تاريح_الحجز = models.DateField(default=date.today)
    id = models.AutoField(primary_key=True)
    رقم_التليفون = models.CharField(max_length=20)    
    الحالة = models.CharField(max_length=100, null=True, blank=True)    

    def __str__(self):
        return self.الاسم

    class Meta:
        verbose_name = 'حقل'
        verbose_name_plural = 'طفل'
