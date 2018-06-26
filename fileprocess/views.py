from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import imgSlide

@csrf_exempt
# Create your views here.
def index(request):
    flinfo = {}
    if request.method == 'POST':
        fl = request.FILES.get('img')
        fl.seek(0, 2)
        flinfo = {'size': fl.tell(),
                  'name': fl.name
        }

        print(flinfo['size'])
        new_img = imgSlide(
            imgfile=fl,
            filename=fl.name
        )
        new_img.save()
    return render(request, 'imgupload/index.html', flinfo)