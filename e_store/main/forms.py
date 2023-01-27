from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from core.views import SignUpView
# from django.urls import reverse_lazy

from .models import Customer
#
# class RegisterForm(UserCreationForm):
#     email = forms.EmailField()
#     password1 = forms.PasswordInput()
#     password2 = forms.PasswordInput()
#
#     class Meta:
#         model = Customer
#         fields = ('username', 'email', 'password1', 'password2')
#
#
# class RegisterView(RegistrationView):
#     form_class = RegisterForm
#     template_name = 'main/register.html'
#     success_url = reverse_lazy('index')
#
#     def form_valid(self, form):
#         email = form.cleaned_data.get('email')
#         username = form.cleaned_data.get('username')
#         new_customer = Customer.objects.create(user=self.request.user, email=email, username=username)
#         return super().form_valid(form)
#
#     def form_invalid(self, form):
#         email = form.cleaned_data.get('email')
#         username = form.cleaned_data.get('username')
#         if Customer.objects.filter(email=email).exists():
#             form.add_error('email', 'email already exists')
#         if Customer.objects.filter(username=username).exists():
#             form.add_error('username', 'username already exists')
#         return super().form_invalid(form)

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email_address = forms.EmailField(max_length=150)
    message = forms.CharField(widget=forms.Textarea,
                              max_length=2000)