from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306199743',
        'name': 'Min Kim',
        'class': 'PBP KKI'
    }

    return render(request, "main.html", context)