from django.db import models
from accounts.models import User
from django_ckeditor_5.fields import CKEditor5Field
from django.urls import reverse


class SafetyArticles(models.Model):
    title = models.CharField(max_length=250)
    content = CKEditor5Field('Content', config_name='extends')
    image = models.ImageField(upload_to='safety/article/', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    category = models.ManyToManyField('SafetyCategory', blank=True)
    date_created = models.DateField(auto_now_add=True)
    is_published = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
    
    
class SafetyCategory(models.Model):
    sub_category = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='sub_cat')
    is_sub_category = models.BooleanField(default=False) 
    title = models.CharField(max_length=200)
    slug = models.SlugField(allow_unicode=True, unique=True, null=True, blank=True)
    image = models.ImageField(upload_to='safety/category', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def get_absolute_url(self):
        return reverse('safety:category', args=[self.id, self.slug])
    
    def __str__(self):
        return self.title
    
    
class SafetyComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(SafetyArticles, on_delete=models.CASCADE)
    comment = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username