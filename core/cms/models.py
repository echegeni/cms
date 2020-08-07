from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User

# Create your models here.
class post (models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان")
    description = models.TextField(max_length=1000, verbose_name="محتوا")
    date = models.DateTimeField(auto_now_add= True, verbose_name="زمان انتشار")
    thumbnail = models.ImageField(upload_to='images/', verbose_name="تصویر شاخص")
    tags = TaggableManager(verbose_name="برچسب ها")
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name="نویسنده")

    class meta:
        verbose_name = "پست"
        verbose_name_plural = "پست ها"

    def __str__(self):
      return self.title
