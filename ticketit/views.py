from django.shortcuts import render, redirect
from django.core.paginator import Paginator, PageNotAnInteger
from django.template.loader import get_template
from user.models import Ticket, Events
from django.contrib.auth.models import User
import uuid
from django.core.mail import send_mail
from django.contrib import messages




def home(request):
    page = request.GET.get('page', 1)
    events = Events.objects.all()
    paginator = Paginator(events,24)
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    return render(request,'ticketit/index.html',{
        'items': items
    })

def movies(request):     
    page = request.GET.get('page', 1)
    events = Events.objects.all()
    paginator = Paginator(events,24)
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    return render(request,'ticketit/movies.html',{
        'items': items
    })



def BuyTicket(request, item_id):
    if request.method == 'GET':
        try:
            item = Events.objects.get(id=item_id)
            if request.GET.get('count'):
                count = request.GET.get('count')
        except Events.objects.get(id=item_id) is None:
            print('Can not find Event')
        return render(request, 'ticketit/buy-confirmation.html', {'item':item, 'count': count})
    
def BuyConfirm(request, item_id, count):
    user = User.objects.get(email=request.user.email)
    ticketits = []
    if Events.objects.get(id=item_id):
        movie = Events.objects.get(id=item_id)
        for i in range(0,count):
            uuidCode = uuid.uuid1()
            ticket = Ticket(user=user, movie=movie, code = str(uuidCode)[:16])
            ticket.save()
            # send_mail(
            #     'Tickets Purchased',
            #     'Here is the message.',
            #     'from@example.com',
            #     ['to@example.com'],
            #     fail_silently=False,
            # )
            ticketits.append({
                'date':movie.date,
                'code':ticket.code,
                'title':movie.title,
                'description':movie.description,
            })
        
        # Send Email
        
        return render(request, 'ticketit/buy-confirmed.html',{ 'items': ticketits})

            
    else:
        messages.info(request, f'Movie not found')
        return redirect('buy-confirmation')
    
        

def sendEmail():
    htmly = get_template('ticketit/Email.html')