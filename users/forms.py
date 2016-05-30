
from django.forms import ModelForm
from django.forms.widgets import DateInput
from .models import CustomUser


class NewUserForm(ModelForm):

    class Meta:
        model = CustomUser
        fields = ['username', 'date_of_birth']
        widgets = {'date_of_birth': DateInput}


class EditUserForm(ModelForm):

    class Meta:
        model = CustomUser
        fields = ['date_of_birth']
        widgets = {'date_of_birth': DateInput}
