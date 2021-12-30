from django.shortcuts import render, redirect,reverse,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from ticket.forms import TicketForm, ResponseForm, UserRegistrationForm, ResponseUpdateForm, TicketUpdateForm
from django.contrib import messages
from .models import Company, Type, Ticket, Response
from django.contrib.auth.models import auth,User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout


# Create your views here.
@login_required(login_url='login_view')
def index(request):
    name = request.user
    form1 = TicketForm()
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            messages.success(request, "Ticket Successfully Generated")
            return HttpResponseRedirect(reverse('index'))

    else:
        form = TicketForm()

    context = {
        'form1': form1,
        'form': form,
        'name': name,
    }

    return render(request, "index.html", context)

@login_required(login_url='login_view')
def remaining_ticket(request):
    tic = Response.objects.exclude(reply='Solved').order_by('ticket__prior')
    comp = Company.objects.all()

    context = {
        'tic': tic,
        'comp': comp,
    }

    return render(request, 'remaining.html', context)

@login_required(login_url='login_view')
def remaining_tickets(request, pk):
    comp = Company.objects.all()
    tic = Response.objects.filter(ticket__company_id = pk).exclude(reply='Solved').order_by('ticket__prior')

    context = {
        'tic': tic,
        'comp': comp,
    }

    return render(request, 'remaining.html', context)

@login_required(login_url='login_view')
def response(request):
    form1 = ResponseForm()

    if request.method == "POST":
        form = ResponseForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()

    else:
        form = ResponseForm()

    resp = Response.objects.all()

    context = {
        'form': form,
        'form1': form1,
        'response': resp,
    }

    return render(request, 'Response.html', context)

def register(request):
    if request.method == 'POST':
        f = UserRegistrationForm(request.POST)
        if f.is_valid():
            user = f.save()
            messages.success(request, 'Account created successfully')
            return redirect('login_view')

    else:
        f = UserRegistrationForm()

    return render(request, 'register.html', {'form': f})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout(request):
    auth.logout(request)
    return redirect('login_view')

@login_required(login_url='login_view')
def show_ticket(request):
    tic = Ticket.objects.order_by('prior')
    comp = Company.objects.all()

    context = {
        'tic': tic,
        'comp': comp,
    }

    return render(request, 'Tickets.html', context)

@login_required(login_url='login_view')
def show_tickets(request, pk):
    tic = Ticket.objects.filter(company_id=pk).order_by('prior')
    comp = Company.objects.all()

    context = {
        'tic': tic,
        'comp': comp,
    }

    return render(request, 'Tickets.html', context)

@login_required(login_url='login_view')
def update_ticket(request,pk):
    form = TicketUpdateForm()
    tic = get_object_or_404(Ticket, id=pk)
    form1= TicketUpdateForm(data=request.POST, instance=tic)
    if form1.is_valid():
        #form1= form1.save(commit=False)
        form1.save()
        return redirect('show_ticket')

    return render(request,'update ticket.html', {'form':form})


def response_update(request,pk):
    form = ResponseUpdateForm(request.POST)
    tic = get_object_or_404(Response, id=pk)

    form1 = ResponseUpdateForm(request.POST, instance=tic)
    if form1.is_valid():
        form1.save()
        return redirect('response')

    return render(request,'response_update.html', {'form':form})
