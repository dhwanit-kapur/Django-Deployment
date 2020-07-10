from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {'text':"You'll never walk alone!", 'number':2020}
    return render(request, 'basic_app/index.html', context_dict)

def other(request):
    return render(request, 'basic_app/other.html')

def relative_url(request):
    return render(request, 'basic_app/relative_url.html')
