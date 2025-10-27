from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class Modal(models.Model):
    title = models.CharField(max_length=200)
    content = CKEditor5Field('Content', config_name='extends')
    date_created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title