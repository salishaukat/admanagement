from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import AdForm
from .models import Ad
from django.db.models import Count, Sum
from random import randint

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


@login_required
def add_advertisement(request):
    form = AdForm(request.POST)
    if form.is_valid():
        obj=form.save(commit=False)
        obj.createdby = request.user
        obj.save()
        return redirect('dashboard')
    return render(request, 'add_advertisement.html', {'form': form})


@login_required
def index(request):
    top_ads_records = Ad.objects.order_by('-display_count')[:10]
    top_ads_records_by_user = Ad.objects.order_by('-display_count').filter(createdby=request.user.id)[:10]
    count = Ad.objects.count()
    random_ad = Ad.objects.all()[randint(0, count - 1)]
    random_ad.display_count = random_ad.display_count + 1
    random_ad.save()
    top_categories = Ad.objects.values('category_id__categoryName').annotate(Count('pk'),sum_displayed=Sum('display_count')).order_by('-sum_displayed')[:5]

    return render(request, 'dashboard.html', {'top_ads_records': top_ads_records,'top_ads_records_by_user': top_ads_records_by_user,'random_ad':random_ad,'top_categories':top_categories})

# Create your views here.
