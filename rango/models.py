from django.contrib.auth.decorators import login_required
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

from django.http import HttpResponse



class Category(models.Model):
    NAME_MAX_LENGTH = 128

    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)



    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


    class Meta:
        verbose_name_plural = 'Categories'


    def __str__(self):
        return self.name

class Page(models.Model):
    TITLE_MAX_LENGTH = 128
    URL_MAX_LENGTH = 200


    category = models.ForeignKey(Category, on_delete=models.CASCADE) 
    title = models.CharField(max_length=128) 
    url = models.URLField() 
    views = models.IntegerField(default=0)
    sum = models.IntegerField(default=0)
    num =models.IntegerField(default=0)
    ave = models.FloatField(default=0)
    slug = models.SlugField(unique=True)
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Page, self).save(*args, **kwargs)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    website = models.URLField(blank=True) 
    picture = models.ImageField(upload_to='profile_images', blank=True)


    def __str__(self):
        return self.user.username


    
