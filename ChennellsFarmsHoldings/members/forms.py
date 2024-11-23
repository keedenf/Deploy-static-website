from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterUserForm(UserCreationForm):
    """Extends the built-in UserCreationForm to add an email field and 
    customize the appearance of form fields using Bootstrap CSS classes.

    **Fields:**

    - 'email': An EmailField for user's email address.
    - 'first_name': A CharField for user's first name.
    - 'last_name': A CharField for user's last name.

    **Meta class:**

    - 'model': Specifies the User model to be used.
    - 'fields': Defines the fields to be included in the form.

    **__init__ method:**

    - Customizes the appearance of all form fields by adding the 'form-control' class to their widgets.
    """
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'