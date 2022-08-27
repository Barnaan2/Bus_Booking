from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.models import User
from .models import Booking
from bus_admin.models import Route,  Single_Bus, Seat, SubRoute
from system_admin.models import Bus
from django.contrib.auth.forms import UserCreationForm
### please do not import all classes from .models because there may be error while login

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    q=request.GET.get('q') if request.GET.get('q') != None else ''
    routes=Route.objects.filter(
    
        Q(name__icontains=q) |
        Q(start__icontains=q) |
        Q(destination__icontains=q)|
        Q(travel_date__icontains=q)
        )
    
    context={'routes':routes}
    return render(request, 'customer/home.html', context)


def route(request, pk):
    route=Route.objects.get(id=pk)
    subroutes=route.subroute_set.all()
   
    context={'route':route, 'subroutes':subroutes}
    return render(request, 'customer/route.html', context)

def booking(request, pk):
    
    subroute=SubRoute.objects.get(id=pk)
    if request.method=='POST':
    
        book=Booking.objects.create(
        user=request.user,
        route=subroute.main_route,
        bus=subroute.bus,
        start=subroute.main_route.start,
        destination=subroute.main_route.destination,
        travel_date=subroute.main_route.travel_date,
        travel_begin_time=subroute.main_route.travel_begin_time,
        travaler_name=request.POST['travaler_name'],
        traveler_contact=request.POST['traveler_contact'],
        seat=request.POST.get('seat'),
        
        )
        return redirect ('my-booking', pk=request.user.id)
    
    context={}
    return render(request, 'customer/booking.html', context)
    
    
def myBooking(request, pk):
    user=User.objects.get(id=pk)
    bookings=user.booking_set.filter().order_by('-created')
    
    context={'bookings':bookings}
    return render(request, 'customer/my_booking.html', context)

def loginPage(request):
    page='login'
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        try:
             user=User.objects.get(username=username)
           
        except:
            messages.error(request, 'Sorry! User does not exist.')
        user=authenticate(request, username=username, password=password)
        
        if user is not None:
           
            login(request, user)
            return redirect('home')
        else :
          messages.error(request, 'Sorry! username or password does not exist.')  
    context={'page':page}
    return render(request, 'customer/login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')


def registerPage(request):
    page='register'
    form=UserCreationForm()
    
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.is_active = True
            user.save()
            return redirect('home')
        else:
            messages.error(request, "An error occured during registration")
    context={'page':page, 'form':form}
    return render(request, 'customer/login_register.html', context)