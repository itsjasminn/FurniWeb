from django.forms import ModelForm
from django.forms.fields import EmailField, CharField
from django.forms.forms import Form
from django.forms.widgets import TextInput, EmailInput, Textarea

from apps.models import User, Message


class EmailForm(Form):
    email = EmailField()


class LoginModelForm(Form):
    email = EmailField(label='Email')
    sms = CharField(label='SMS Code')

    class Meta:
        model = User
        fields = 'email', 'sms',

    def validate_user(self):
        user = self.cleaned_data['email']
        return user

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['first_name', 'last_name', 'email', 'message']
        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'message': Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message', 'rows': 5}),
        }
