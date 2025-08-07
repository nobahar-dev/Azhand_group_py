from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import *


def request_ticket(request):
    tickets = Ticket.objects.filter(user=request.user).order_by('-date_created')
    user = request.user
    context = {
        'user': user,
        'tickets': tickets
    }
    return render(request, 'ticketing/request_ticket.html', context)


def new_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            messages.success(request, 'در خواست شما با موفقیت ثبت گردید')
            return redirect('ticketing:request_ticket')
        else:
            messages.error(request, 'مشکلی در ارسال درخواست شما رخ داده است')
    else:
        form = TicketForm()
    
    user = request.user
    context = {
        'form': form,
        'user': user
    }
    return render(request, 'ticketing/new_ticket.html', context)


def ticket_detail(request, ticket_id):
    referer = request.META.get('HTTP_REFERER')
    
    ticket = get_object_or_404(Ticket, id=ticket_id)
    replies = TicketReply.objects.filter(ticket_id=ticket_id)
    user = request.user
    
    if request.method == 'POST':
        form = TicketReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.user = user
            reply.ticket = ticket
            reply.save()
            messages.success(request, 'پاسخ شما با موفقیت ثبت شد.')
            return redirect(referer)
        else:
            messages.success(request, 'مشکلی در ارسال پاسخ شما رخ داده است')
    else:
        form = TicketReplyForm()
    
    context = {
        'ticket': ticket,
        'replies': replies,
        'user': user,
        'form': form
    }
    return render(request, 'ticketing/ticket_detail.html', context)