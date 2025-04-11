from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator
from .forms import ContactForm
from .models import ContactRequest, Car

def index(request):
    cars_list = Car.objects.all().order_by('-id')
    paginator = Paginator(cars_list, 6)
    page_number = request.GET.get('page')
    cars = paginator.get_page(page_number)
    
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            ContactRequest.objects.create(
                name=form.cleaned_data['name'],
                phone=form.cleaned_data['phone'],
                message=form.cleaned_data['message']
            )
            return redirect('success_page')
    else:
        form = ContactForm()

    return render(request, "index.html", {
        "form": form,
        "cars": cars
    })

def about(request):
    return render(request, "about.html")

def success_page(request):
    return render(request, "success.html")

def contact_ajax(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            ContactRequest.objects.create(
                name=form.cleaned_data['name'],
                phone=form.cleaned_data['phone'],
                message=form.cleaned_data['message']
            )
            return JsonResponse({'status': 'success'})
        return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
    return JsonResponse({'status': 'error'}, status=405)

def new_cars(request):
    cars = Car.objects.filter(year__gte=2023).order_by('-id')
    return render(request, 'catalog.html', {'cars': cars, 'title': 'Новые автомобили'})

def used_cars(request):
    cars = Car.objects.filter(year__lt=2023).order_by('-id')
    return render(request, 'catalog.html', {'cars': cars, 'title': 'Автомобили с пробегом'})

def promo_cars(request):
    cars = Car.objects.filter(discount__gt=0).order_by('-id')
    return render(request, 'catalog.html', {'cars': cars, 'title': 'Акционные предложения'})