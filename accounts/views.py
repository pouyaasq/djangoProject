from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import login,logout
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():#shart haye form reayat shode bod
            user = form.save()
            login(request, user)
            return redirect('articels:list')#bro be...
    else:
        form = UserCreationForm()#form khali
    return render(request,'accounts/signup.html',{'form':form})
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:#agar moyabegh html mikhaste be safhe digari bere
                return redirect(request.POST.get("next"))#request.POST:tamam chizhaye ersal shode tavasot user,get("next"):daryafet next(be che safhe mikhste bere)
            else:
                return redirect('articels:list')
    else:
        form = AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('articels:list')
