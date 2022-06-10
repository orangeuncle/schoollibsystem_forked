from django.shortcuts import render

# Create your views here.

def index(request):
    req = request
    template = "library/index.html"
    context = {}
    return render(req, template, context)