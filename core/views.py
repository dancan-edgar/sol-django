from django.shortcuts import render

# Create your views here.
def index(request):
    context = {'segment': 'index'}
    return render(request, 'core/index.html', context)