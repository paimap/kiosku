from django.shortcuts import render, redirect
from main.forms import StockEntryForm
from main.models import StockEntry
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_main(request):
    stock_entries = StockEntry.objects.all()
    context = {
        'npm' : '2306275986',
        'nama': 'Paima Ishak Melkisedek Purba',
        'kelas': 'PBP E',
        'stock_entry': stock_entries
    }

    return render(request, "main.html", context)

def create_stock_entry(request):
    form = StockEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_stock_entry.html", context)

def show_xml(request):
    data = StockEntry.objects.all()
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