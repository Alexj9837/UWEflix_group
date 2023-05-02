from django import forms
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row
from .models.booking import Booking
from .models.account import User, Representitive
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

class ClubForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = [
            "club_name",
            "street_number",
            "street",
            "city",
            "post_code",
            "landline_number",
            "mobile_number",
            "email",
            "first_name",
            "last_name",
            "dob",
        ]


class filmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = [
            "name",
            "image",
            "date",
            "duration",
            "type",
            "language",
            "rating",
            "cast",
            "trailer",
            "up",
            "price",

        ]


class screenForm(forms.ModelForm):
    class Meta:
        model = Screen
        fields = [
            "screen_number",
            "capacity",
        ]


class showForm(forms.ModelForm):
    class Meta:
        model = Show
        fields = [
            "screen",
            "date",
            "time",
            "film",
        ]

class ClubRegistrationForm(forms.Form):
    name = forms.CharField(label='Club name', max_length=255)
    address = forms.CharField(label='Address', max_length=255,
                              widget=forms.TextInput(
                                  attrs={'placeholder': 'Street, City, Postcode'})
                              )
    contact_details = forms.CharField(label='Contact details', max_length=255)
    first_name = forms.CharField(label='First name', max_length=255)
    last_name = forms.CharField(label='Last name', max_length=255)
    date_of_birth = forms.DateField(
        label='Date of birth', widget=forms.SelectDateWidget(years=range(1900, 2020)))

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        address = cleaned_data.get('address')
        contact_details = cleaned_data.get('contact_details')
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        date_of_birth = cleaned_data.get('date_of_birth')
        if not name and not address and not contact_details and not first_name and not last_name and not date_of_birth:
            raise forms.ValidationError('You have to write something!')


class TicketPurchaseForm(forms.Form):
    show = forms.ModelChoiceField(queryset=Show.objects.all())
    payment_details = forms.CharField(label='Payment details', max_length=255)

    def clean(self):
        cleaned_data = super().clean()
        show = cleaned_data.get('show')
        payment_details = cleaned_data.get('payment_details')
        if not show and not payment_details:
            raise forms.ValidationError('You have to write something!')

class RepForm(forms.ModelForm):
    # Form for representitive
    class Meta:
        model = Representitive
        fields = [
            "firstName",
            "lastName",
            "DateOfBirth",
            "password",
            "affiliatedClub",
           # "studentRepresentitive",
        ]
        widgets = {
            'password': forms.TextInput(
                attrs={
                    'placeholder': 'Enter a password',
                    'type': 'password'
                }
            )
        }

class UserForm(forms.ModelForm):
    # Form for User model
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'dateOfBirth': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={'class': 'form-control',
                    'placeholder': 'Select a date',
                    'type': 'date'
                }),
            'password': forms.TextInput(
                attrs={
                    'placeholder': 'Enter a password',
                    'type': 'password'
                }
            )
        }