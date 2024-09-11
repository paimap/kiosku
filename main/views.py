from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306275986',
        'nama': 'Paima Ishak Melkisedek Purba',
        'kelas': 'PBP E'
    }

    return render(request, "main.html", context)