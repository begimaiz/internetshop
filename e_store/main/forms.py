from django import forms
from .models import Customer


# class LoginForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)



    class Meta:
        model = Customer
        fields = ('username', 'email', 'password')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = Customer.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("username is taken")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = Customer.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is taken")
        return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password2 != password:
            raise forms.ValidationError("Passwords must match.")
        return data


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email_address = forms.EmailField(max_length=150)
    message = forms.CharField(widget=forms.Textarea,
                              max_length=2000)