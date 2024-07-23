from django.db import models

# Create your models here.

class Doginfo(models.Model):
    GEND=(("1","Male"),("2","Female"))
    VAC=(("1","Done"),("2","Pending"))
    breed_name=models.CharField(max_length=30,verbose_name="Breed")
    gender=models.CharField(max_length=30,verbose_name="Gender",choices=GEND)
    age=models.FloatField(verbose_name="Months")
    vaccine=models.CharField(max_length=40,verbose_name="Vaccination",choices=VAC)
    price=models.FloatField(verbose_name="Quote")
    uid=models.IntegerField()

    def __str__(self):
        return self.breed_name
        # return self.gender
        # return self.age
        # return self.vaccine
        # return self.price
        # return self.uid