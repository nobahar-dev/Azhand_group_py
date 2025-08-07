from django.db import models
from accounts.models import User


class Ticket(models.Model):
    STATUS_CHOICE = [
        ('open', 'باز'),
        ('in_progress', 'در حال رسیدگی'),
        ('completed', 'انجام شد'),
        ('aborted', 'لغو شده')
    ]
    
    COMPANY_CHOICE = [
        ('avicenna', 'کارخانه دارو سازی آوه سینا'),
        ('arasto', 'کارخانه دارو سازی ارسطو')
    ]
    
    UNIT_CHOICES = [
        ('qa', 'واحد تضمین کیفیت'),
        ('storage', 'واحد انبار'),
        ('production', 'واحد تولید'),
        ('manager', 'مدیریت کارخانه'),
        ('office', 'واحد اداری'),
        ('technical', 'واحد فنی')
    ]
    
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=250)
    description = models.TextField()
    status = models.CharField(max_length=200, choices=STATUS_CHOICE, default='open')
    company = models.CharField(max_length=200, choices=COMPANY_CHOICE, default='avicenna')
    unit = models.CharField(max_length=200, choices=UNIT_CHOICES, default='manager')
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    
class TicketReply(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='replies')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    message = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.ticket.title