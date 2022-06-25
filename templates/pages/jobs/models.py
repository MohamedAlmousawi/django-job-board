from django.db import models
from django.utils.text import slugify
# Create your models here.
from django.contrib.auth.models import User
class Job(models.Model):
    x= {
        ('Full-Time','Full-time'),
        ('Part-Time','Part-Time'),

    }
    category = models.ForeignKey("Category", on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(max_length = 100,null=True,blank=True)
    job_type = models.CharField(max_length = 50,choices=x,null=True,blank=True)
    pulished_at = models.DateTimeField(auto_now=True)
    description = models.TextField(max_length=500,null=True,blank=True)
    vacancy = models.IntegerField(null=True,blank=True)
    salary = models.IntegerField(null=True,blank=True)
    image = models.ImageField(upload_to='job_images', null=True,blank=True)
    slug = models.SlugField(max_length = 50,null=True,blank=True)
   

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Job, self).save(*args, **kwargs) # Call the real save() method

class Category(models.Model):
    category  = models.CharField(max_length = 150)
    def __str__(self):
        return self.category


class Apply(models.Model):
    job= models.ForeignKey(Job, on_delete=models.CASCADE)
    name  = models.CharField(max_length = 150)
    email = models.EmailField(max_length=50)
    website  = models.URLField(max_length = 200)
    cv = models.FileField(upload_to='job_cv')
    cover_letter = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name


