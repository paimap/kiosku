from django.shortcuts import render, redirect, reverse
from main.forms import StockEntryForm
from main.models import StockEntry
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags


from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    context = {
        'name': request.user.username,
        'npm' : '2306275986',
        'nama': 'Paima Ishak Melkisedek Purba',
        'kelas': 'PBP E',
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

def create_stock_entry(request):
    form = StockEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        stock_entry = form.save(commit=False)
        stock_entry.user = request.user
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_stock_entry.html", context)

def show_xml(request):
    data = StockEntry.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = StockEntry.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = StockEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = StockEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)
      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
   else:
      messages.error(request, "Invalid username or password. Please try again.")
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_stock(request, id):
    print(f"Received ID: {id}")
    # Get stock entry berdasarkan id
    stock = StockEntry.objects.get(pk = id)

    # Set stock entry sebagai instance dari form
    form = StockEntryForm(request.POST or None, instance=stock)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_stock.html", context)

def delete_stock(request, id):
    # Get stock berdasarkan id
    stock = StockEntry.objects.get(pk = id)
    # Hapus stock
    stock.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
@require_POST
def add_stock_entry_ajax(request):
    name = strip_tags(request.POST.get("name"))
    description = strip_tags(request.POST.get("description"))
    price = request.POST.get("price")
    quantity = request.POST.get("quantity")
    user = request.user

    new_stock = StockEntry(
        name = name, description = description,
        price = price, quantity = quantity,
        user=user
    )
    new_stock.save()

    return HttpResponse(b"CREATED", status=201)

@csrf_exempt
def create_mood_flutter(request):
    if request.method == 'POST':

        data = json.loads(request.body)
        new_mood = ProductEntry.objects.create(
            user=request.user,
            mood=data["mood"],
            mood_intensity=int(data["mood_intensity"]),
            feelings=data["feelings"]
        )

        new_mood.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)