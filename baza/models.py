from django.db import models
from django.utils import timezone


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=News.Status.Published)

class Category(models.Model):
    name = models.CharField(max_length=100,verbose_name="Kategoriya",help_text="Ma'lumot yo'nalishlari")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Yo'nalishlar"


class News(models.Model):
    class Status(models.TextChoices):
        Draft = "DF",'Draft'
        PUBLISHED = "PD",'Published'

    title=models.CharField(max_length=250,verbose_name="Xabar",help_text="Title of the news")
    slug=models.CharField(max_length=250,verbose_name="Url shakli",help_text="O'zi-ozini to'ldiradi")
    body=models.TextField(verbose_name="Asosiy qismi")
    image=models.ImageField(upload_to='news/images')
    category=models.ForeignKey(Category,on_delete=models.CASCADE,)
    pulish_time=models.DateTimeField(default=timezone.now)
    create_time=models.DateTimeField(auto_now_add=True)
    update_time=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=2,choices=Status.choices,default=Status.Draft)
    class Meta:
       ordering=['-update_time',]
       verbose_name_plural="Yangiliklar"
    def __str__(self):
        return self.title

class Contact(models.Model):
    name=models.CharField(max_length=300,verbose_name="Kontak")
    email=models.CharField(max_length=300,verbose_name="Email")
    message=models.TextField()
    def __str__(self):
        return self.name





