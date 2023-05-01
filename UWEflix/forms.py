from django import forms
from .models import Booking, Club, Screen, Show, Film

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

# class bookingForm(forms.ModelForm):
#     class Meta:
#         model = Booking
#         fields = [
#             "seat_number",
#             "ticket_type",
#             "quantity",
#             "card_number",
#         ]


# class bookingForm(forms.ModelForm):
#     class Meta:
#         model = Booking
#         fields = ['email', 'name', 'mobile', 'age', 'seats']
#         labels = {
#             'email': 'Email',
#             'name': 'Name',
#             'mobile': 'Mobile Number',
#             'age': 'Age',
#             'seats': 'Number of Seats'
#         }
#         widgets = {
#             'email': forms.EmailInput(attrs={'class': 'form-control'}),
#             'name': forms.TextInput(attrs={'class': 'form-control'}),
#             'mobile': forms.NumberInput(attrs={'class': 'form-control'}),
#             'age': forms.NumberInput(attrs={'class': 'form-control'}),
#             'seats': forms.NumberInput(attrs={'class': 'form-control'})
#         }

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.layout = Layout(
#             Row(
#                 Column('name', css_class='form-group col-md-6 mb-0'),
#                 Column('email', css_class='form-group col-md-6 mb-0'),
#                 css_class='form-row'
#             ),
#             Row(
#                 Column('mobile', css_class='form-group col-md-6 mb-0'),
#                 Column('age', css_class='form-group col-md-6 mb-0'),
#                 css_class='form-row'
#             ),
#             Row(
#                 Column('seats', css_class='form-group col-md-12 mb-0'),
#                 css_class='form-row'
#             ),
#             Submit('submit', 'Submit')
#         )


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


class screenForm(forms.ModelForm):
    class Meta:
        model = Screen
        fields = [
            "screen_number",
        ]


class showForm(forms.ModelForm):
    class Meta:
        model = Show
        fields = [
            "date",
            "time",
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


class LoginForm(forms.Form):
    rep_no = forms.CharField(label='Representative Number', max_length=255)
    password = forms.CharField(
        label='Password', max_length=255, widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        rep_no = cleaned_data.get('rep_no')
        password = cleaned_data.get('password')
        if not rep_no and not password:
            raise forms.ValidationError('You have to write something!')
