from django.shortcuts import render

# Create your views here.


def fiter_method(request):
    d={'data':'My Name iS mAHESH'}
    return render(request,'filtermethod.html')