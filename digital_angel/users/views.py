from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        # we need to validate data
        if form.is_valid():
            # this saves data to DB
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created. You are now able to login.')
            return redirect('login')
    else:
        # form = UserCreationForm()
        form = UserRegisterForm()
    return render(request, 'users/register.html', { 'form': form })

# can be seen only when logged in
# for class views this way doesn't work
@login_required
def profile(request):
    return render(request, 'users/profile.html')


# all the possible messages
# messages.debug
# messages.info
# messages.success
# messages.warning
# messages.error
