from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Post(models.Model):

    imie = models.CharField(max_length=200)
    tagi = models.TextField(blank=True)
    e_mail = models.EmailField(blank=True)
    telefon = PhoneNumberField(blank=True,region='PL')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)



    def __str__(self):
        return self.title