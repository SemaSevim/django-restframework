from tkinter import CASCADE
from turtle import title
from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=250)

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published') 
    def __str__(self):
        return self.question_text()

 #   def was_published_recently(self):
#      return self.pub_date >= timezone.now() - datetime.timedelta(days=1)      

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE )       
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self) :
        return self.choice_text, self.question, 

class Makale(models.Model):
    yazar = models.CharField(max_length = 150)   
    baslik = models.CharField(max_length=120)
    aciklama = models.CharField(max_length=200)
    metin = models.TextField()
    sehir = models.BooleanField(default=True)
    yayımlanma_tarihi = models.DateField()
    aktif =  models.BooleanField(default=True)
    yaratilma_tarihi = models.DateTimeField(auto_now_add=True)
    güncelleme_tarihi = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.baslik
