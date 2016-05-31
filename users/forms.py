
from django.forms import ModelForm, widgets
from .models import CustomUser


class NewUserForm(ModelForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'date_of_birth')

        widgets = {
            'username': widgets.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Username'}),

            'first_name': widgets.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'First name'}),

            'last_name': widgets.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Last name'}),

            'email': widgets.EmailInput(
                attrs={'class': 'form-control', 'placeholder': 'Email'}),

            'date_of_birth': widgets.DateInput(
                format='%Y-%m-%d', attrs={'class': 'form-control'})
        }


class EditUserForm(NewUserForm):

    class Meta(NewUserForm.Meta):
        exclude = ('username',)
