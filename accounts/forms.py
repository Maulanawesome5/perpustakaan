# from django import forms
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from .models import CustomUser


# class CustomUserCreationForm(UserCreationForm):
#     """
#     Merupakan class untuk menampilkan elemen formulir HTML untuk registrasi akun baru.
#     Class ini mewarisi (inherit) dari class bawaan Django `UserCreationForm`.
#     Formulir default / bawaan yang tersedia adalah:
#         - username -> label, input, help_text
#         - password1 -> label, input, help_text
#         - password2 -> label, input, help_text
#     """
#     class Meta:
#         model = CustomUser
#         fields = ("first_name", "last_name", "username", "email")


# class CustomUserChangeForm(UserChangeForm):
#     class Meta:
#         model = CustomUser
#         fields = ("username", "email")
