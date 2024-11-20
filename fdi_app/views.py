from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, TranferForm
from .models import Tranfer
from django.contrib.auth.decorators import login_required
# from django.shortcuts import render, redirect
# from .forms import RegistrationForm

# Create your views here.
def HomePage(request):
    return render(request, 'main/index.html')

def AboutUs(request):
    return render(request, 'main/about.html')

def ContactUS(request):
    return render(request, 'main/contact.html')

def Service(request):
    return render(request, 'main/service.html')

def Guard(request):
    return render(request, 'main/guard.html')


@login_required
def Logout_Confirm(request):
    return render(request, 'main/logout.html')


@login_required
def history(request):
    transfers = Tranfer.objects.all().order_by('-date_created')
    return render(request, 'main/history.html', {'transfers':transfers})



def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been created! You can now log in.")
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'main/register.html', {'form': form})


# @login_required
# def profile(request):
#     if  request.method == 'POST':
#         p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
#         if p_form.is_valid():
#             p_form.save()
#             messages.success(request, f'Your account is updated')
#             return redirect('profile')
#     else:
#         p_form = ProfileUpdateForm(instance=request.user.profile)
#     context = {
#         'p_form' : p_form
#     }
#     return render(request, 'main/profile.html', context)


@login_required
def transfer_money(request):
    if request.method == "POST":
        form = TranferForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Money Transferred successfully')
            return redirect('profile')
    else:
        form = TranferForm()
    context = {'form': form}
    return render(request, 'main/profile.html', context)



# @login_required
# def recent_transfer(request):
#     transfers = Tranfer.objects.all()
#     return render(request, 'main/history.html', {'transfers':transfers})
    