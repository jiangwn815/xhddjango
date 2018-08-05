from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from .models import imgSlide, UploadFile
from datetime import datetime



@login_required()
@csrf_exempt
# Create your views here.
def index(request):
    flinfo = {}
    if request.method == 'POST':
        fl = request.FILES.get('img')
        fl.seek(0, 2)  # 挪到文件末尾
        flinfo = {
            'size': fl.tell(),  # 获取文件大小
            'name': fl.name
        }
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
        print("上传用户：", request.user)
        print("上传时间：", datetime.now())
        print("上传文件：", flinfo["name"])
        print("文件大小(KB)：", flinfo["size"]/1024)
        print("上传路径：", uf.filedata.path)

    return render(request, 'imgupload/index.html', flinfo)
