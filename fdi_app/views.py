from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserUpdateForm, ProfileUpdateForm, UserRegisterForm
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




# def register(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')  # Redirect to login page after successful registration
#     else:
#         form = RegistrationForm()
#     return render(request, 'main/register.html', {'form': form})


@login_required
def Logout_Confirm(request):
    return render(request, 'main/logout.html')


@login_required
def history(request):
    return render(request, 'main/history.html')







# Create your views here.

def register(request):
    if  request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to login')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'main/register.html', {'form': form})


# def logout_confirm(request):
#     return render(request, 'main/logout.html')

@login_required
def profile(request):
    if  request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if p_form.is_valid() and u_form.is_valid() :
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account is updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }
    return render(request, 'main/profile.html', context)
