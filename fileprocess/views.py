from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import imgSlide

@csrf_exempt
# Create your views here.
def index(request):
    if request.method == 'POST':
        fl = request.FILES.get('img')
        fl.seek(0, 2)
        print(fl.tell())
        new_img = imgSlide(
            imgfile = request.FILES.get('img'),
            filename = request.FILES.get('img').name
        )
        new_img.save()
    return render(request, 'imgupload/index.html')