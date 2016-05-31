
from django.forms import ModelForm, widgets
from .models import CustomUser


class NewUserForm(ModelForm):

    class Meta:
        model = CustomUser
        fields = ['username', 'date_of_birth']

        widgets = {
            'username': widgets.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Username'}),

            'date_of_birth': widgets.DateInput(
                format='%Y-%m-%d', attrs={'class': 'form-control'})
        }


class EditUserForm(ModelForm):

    class Meta:
        model = CustomUser
        fields = ['date_of_birth']

        widgets = {
            'date_of_birth': widgets.DateInput(
                format='%Y-%m-%d', attrs={'class': 'form-control'})
        }
