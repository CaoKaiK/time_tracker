from django.shortcuts import render

# Create your views here.

def testView(request):
    return render(request, 'dashboard/flextime.html')