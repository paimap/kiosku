from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name' : 'Smartphone',
        'price': 2000000,
        'description': 'Smartphone dengan layar AMOLED 6.7 inci, prosesor Octa-Core, 128GB storage, dan kamera 64MP.'
    }

    return render(request, "main.html", context)