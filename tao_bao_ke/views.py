from django.shortcuts import render
from tao_bao_ke import views
from tao_bao_ke import models
# Create your views here.

def index(request):

    if request.method == 'POST':
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)

        models.user_info.objects.create(user=username,pwd=password)
    user_list = models.user_info.objects.all()
    #return render(request,'index.html')
    return render(request,'index.html',{'data':user_list})
'''
def shang_pin_shu_ju():
    data_list = models.shang_pin_shu_ju.objects.all()
    return data_list
'''
def home(request):
    request_lei_mu = []
    #values 返回一个数据列表，并可限制字段
    request_lei_mu_dict_list = models.LeiMuDuiZhao.objects.filter(web_lei_mu=1).values('lei_mu')
    #only 作用是立即载入数据，并不是限制字段
    #request_lei_mu = models.LeiMuDuiZhao.objects.only('lei_mu').filter(web_lei_mu=1)
    for i in request_lei_mu_dict_list:
        temp = i['lei_mu']
        request_lei_mu.append(temp)

    data = models.ShangPinShuJu.objects.filter(shang_pin_lei_mu__in=request_lei_mu)[:100]
    #return render(request,'tao_bao_ke.html',{'data':data})
    return render(request, 'home.html', {'data': data})

def search(request):
    if request.method == 'POST':
        if len(request.POST.get('search_value')) > 0:
            search_value = request.POST.get('search_value')
            data = models.ShangPinShuJu.objects.filter(shang_pin_ming_cheng__icontains=search_value)
            if len(data) > 0:
                return render(request,'search.html',{'data':data})
            else:
                return  render(request,'nothing_found.html')
        else:
            return render(request,'search_value.html')
    else:
        return render(request, 'search_value.html')


def rail(request):
    data = models.shang_pin_shu_ju.objects.all()[:5]
    return render(request,'rail.html',{'data': data})


def screen_area(request):
    if request.method =='GET':
        if len(request.GET.get('leimu')) > 0:
            lei_mu = request.GET.get('leimu')
            data = models.shang_pin_shu_ju.objects.filter(id=int(lei_mu))
            return render(request,'screen_area.html',{'data':data})

