from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

#migration göç yapmak demektir.
# Create your models here.
class Musician(models.Model):
    name = models.CharField(max_length=40) #en fazla 40 karakter olacak diyoruz isminin.
    instrument = models.CharField(max_length=30)
    age = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(150)]) #bir insanın yaşı 0'dan küçük olamaz 150'den büyük olamaz.
    salary = models.IntegerField(default= 0, validators[MinValueValidator(0)])

    def __str__(self):
        return f"Name: {self.name}, Instrument: {self.instrument}, Age: {self.age}"

