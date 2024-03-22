"""
Views for user.
"""
from django.contrib.auth import (
    authenticate,
    login,
)
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
)
from django.shortcuts import (
    render,
    redirect,
)
from django.contrib import messages

def register_view(request):
    """Generate form for user registration."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User registered successfuly. Please log in.')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'Error in {field}: {error}')
            return redirect('user:register')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


