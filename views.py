# views.py
from django.shortcuts import render, redirect
from .models import User, Cinema, Session
from .forms import LoginForm, RegisterForm, BuyTicketForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.get(username=username)
            if user.password == password:
                request.session['username'] = username
                return redirect('cinema_list')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def cinema_list(request):
    cinemas = Cinema.objects.all()
    return render(request, 'cinema_list.html', {'cinemas': cinemas})

def cinema_detail(request, cinema_id):
    cinema = Cinema.objects.get(id=cinema_id)
    sessions = Session.objects.filter(cinema=cinema, start_time__date=datetime.date.today())
    return render(request, 'cinema_detail.html', {'cinema': cinema, 'sessions': sessions})

def session_detail(request, session_id):
    session = Session.objects.get(id=session_id)
    return render(request, 'session_detail.html', {'session': session})

def buy_ticket(request, session_id):
    if request.method == 'POST':
        form = BuyTicketForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=request.session['username'])
            session = Session.objects.get(id=session_id)
            seat_number = form.cleaned_data['seat_number']
            if session.available_seats > 0:
                ticket = Ticket(user=user, session=session, seat_number=seat_number)
                ticket.save()
                session.available_seats -= 1
                session.save()
                return redirect('ticket_confirmation')
    else:
        form = BuyTicketForm()
    return render(request, 'buy_ticket.html', {'form': form, 'session': Session.objects.get(id=session_id)})

def ticket_confirmation(request):
    return render(request, 'ticket_confirmation.html')