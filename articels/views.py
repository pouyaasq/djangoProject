from django.shortcuts import render , HttpResponse , redirect
from . import models
from django.contrib.auth.decorators import login_required
from . import forms
def articel_list(request):
    articels = models.Article.objects.all().order_by('-date')#bar asas date daste bandi mi shavad
    args = {'articels':articels}
    return render(request,'articels/articel.html',args)
def articel_detail(request,slug):
    # return HttpResponse(slug)
    articel = models.Article.objects.get(slug=slug)
    return render(request,'articels/articel_detail.html',{'articel':articel})
@login_required(login_url= '/accounts/login')#decorator check mikonad ke login shodim ya na
def articel_create(request):
    if request.method == 'POST':
        form = forms.articelCreate(request.POST,request.FILES)#request.FILES:aks
        if form.is_valid():
            instance = form.save(commit= False)#commit= False:save nemikonad
            instance.author = request.user
            instance.save()
            return redirect('articels:list')
    else:
        form = forms.articelCreate()
    return render(request,'articels/articel_create.html',{'form':form})
