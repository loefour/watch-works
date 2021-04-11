from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRefisterForm, UserUpdateforme, ProfileUpdateForm


def register(request):
    if request.method == 'POST':
        form = UserRefisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'you account has been created you are now able to log in')
            return redirect('login')
    else:
        form = UserRefisterForm()
    return render(request, 'users/register.html', {"form": form})


@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateforme(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f' account has been Updated')
            return redirect('profile')
    else:
        u_form = UserUpdateforme(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)