from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm


# Create your views here.
def login_user(request):
    """Handles user login.

    Args:
        request: The HTTP request object containing the user's login information.

    Returns:
        A Django HTTP response object:
            On successful login: Redirects to a success page (e.g., home page) with a success message in the context.
            On invalid login: Renders the login form again with an error message in the context.
    """
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            context = {'success_message':'You have been successfully logged in.'}
            return render(request, 'main/home.html', context)
        else:
            # Return an 'invalid login' error message.
            context = {'error_message':'There was an error logging in, please try again.'}
            return render(request, 'authenticate/login.html', context)

    else:
        pass
    return render(request, 'authenticate/login.html', {})


def logout_confirmation(request):
    """Handles user logout.

    Args:
        request: The HTTP request object.

    Returns:
        Redirects to the home page with a success message.
    """
    return render(request, 'authenticate/logout.html', {})


def logout_user(request):
    """Handles user logout.

    Args:
        request: The HTTP request object.

    Returns:
        Redirects to the home page with a success message.
    """
    logout(request)
    context = {'success_message':'You have been successfully logged out.'}
    return render(request, 'main/home.html', context)


def register_user(request):
    """Registers a new user and logs them in on successful registration.

    Args:
        request: request object containing user-submitted data.

    Returns:
        A redirect response to the user profile page on successful registration and login.
        A rendered registration form template on GET request or failed form validation.

    Raises:
        ValueError: If required form fields are missing or invalid.
    """
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            context = {'success_message':'You have been successfully registered and logged in.'}
            return render(request, 'main/home.html', context)
    else:
        form = RegisterUserForm()

    return render(request, 'authenticate/register_user.html', {'form':form})

