from django.db import models
from accounts.models import User
from django_ckeditor_5.fields import CKEditor5Field
from django.urls import reverse


class ArastoArticles(models.Model):
    title = models.CharField(max_length=250)
    content = CKEditor5Field('Content', config_name='extends')
    image = models.ImageField(upload_to='arasto/article/', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    category = models.ManyToManyField('ArastoCategory', blank=True)
    date_created = models.DateField(auto_now_add=True)
    is_published = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
    
    
class ArastoCategory(models.Model):
    sub_category = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='sub_cat')
    is_sub_category = models.BooleanField(default=False) 
    title = models.CharField(max_length=200)
    slug = models.SlugField(allow_unicode=True, unique=True, null=True, blank=True)
    image = models.ImageField(upload_to='arasto/category', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def get_absolute_url(self):
        return reverse('arasto:category', args=[self.id, self.slug])
    
    def __str__(self):
        return self.title
    
    
class ArastoComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(ArastoArticles, on_delete=models.CASCADE)
    comment = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username