from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from .models import imgSlide, UploadFile
import os
from django.conf import settings


@login_required()
@csrf_exempt
# Create your views here.
def index(request):
    flinfo = {}
    if request.method == 'POST':
        fl = request.FILES.get('img')
        fl.seek(0, 2)
        flinfo = {
            'size': fl.tell(),
            'name': fl.name
        }
        print(flinfo['size'])
        uf = UploadFile(
            user=request.user,
            filedata=fl,
            filename=fl.name,
            file_type="O"
        )
        #save_path = settings.MEDIA_ROOT + "/" + request.user.__str__() + "/excel/" + new_img.imgfile.name
        #os.rename(new_img.imgfile.path, save_path)
        #new_img.imgfile.path = save_path
        uf.save()
        print(uf.filedata.path)

    return render(request, 'imgupload/index.html', flinfo)