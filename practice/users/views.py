from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username') # just for show
            messages.success(request, f'Account created for {username}, Please login')
            return redirect('login')

    else:
        form = UserRegistrationForm()

    return render(
        request,
        'users/registration.html', 
        context={'form': form}
    )

@login_required
def profile(request):
    if request.method == "POST":
        # request.post is sent to populate the form with request data
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Your account has been updated")
            return redirect('profile') # to avoid the resubmission error
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(
        request,
        'users/profile.html',
        context= context
    )

# Create your views here.
