from django import forms
from .models import *


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('title', 'description', 'company', 'unit')
        
        
class TicketReplyForm(forms.ModelForm):
    class Meta:
        model = TicketReply
        fields = ('message', )