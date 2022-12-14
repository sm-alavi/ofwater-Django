from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    model = User
    field = ('username', 'password')

    widgets = {

        'username': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Username'}),
        'password': forms.PasswordInput(attrs={'class': 'form-control form-control-sm'}),
    }


class UserForms(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name',
                  'last_name', 'email', 'is_superuser', 'is_active')

        widgets = {

            'username': forms.TextInput(attrs={'calss': 'form-control'}),
            'password': forms.PasswordInput(attrs={'calss': 'form-control'}),
            'first_name': forms.TextInput(attrs={'calss': 'form-control'}),
            'last_name': forms.TextInput(attrs={'calss': 'form-control'}),
            'email': forms.EmailInput(attrs={'calss': 'form-control'}),
            'is_superuser': forms.CheckboxInput(attrs={'calss': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'calss': 'form-control'}),

        }


class UserChangeForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',
                  'user_permissions', 'is_superuser', 'is_active')

        widgets = {

            'username': forms.TextInput(attrs={'calss': 'form-control'}),
            'first_name': forms.TextInput(attrs={'calss': 'form-control'}),
            'last_name': forms.TextInput(attrs={'calss': 'form-control'}),
            'email': forms.EmailInput(attrs={'calss': 'form-control'}),
            'is_superuser': forms.CheckboxInput(attrs={'calss': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'calss': 'form-control'}),
            'user_permissions': forms.SelectMultiple(attrs={'calss': 'form-control'})

        }


class UserProfileForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].disabled = True
        self.fields['is_superuser'].disabled = True
        self.fields['is_active'].disabled = True

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',
                  'is_superuser', 'is_active')

        widgets = {

            'username': forms.TextInput(attrs={'calss': 'form-control'}),
            'first_name': forms.TextInput(attrs={'calss': 'form-control'}),
            'last_name': forms.TextInput(attrs={'calss': 'form-control'}),
            'email': forms.EmailInput(attrs={'calss': 'form-control'}),
            'is_superuser': forms.CheckboxInput(attrs={'calss': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'calss': 'form-control'}),
            'user_permissions': forms.SelectMultiple(attrs={'calss': 'form-control'})

        }
