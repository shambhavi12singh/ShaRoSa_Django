from django.db import models
from django.db.models import Sum
class ShaRoSa(models.Model):
    name=models.CharField(max_length=30)
    mail=models.EmailField(unique=True)
    passwrd=models.CharField(max_length=30)
    def _str_(self):
        return self.smail+" "+str(self.spassword)+" "+str(self.sconfrmpasswrd)
class Bill(models.Model):
    item=models.CharField(max_length=30)
    charge=models.IntegerField(max_length=5)