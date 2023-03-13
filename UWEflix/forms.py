from django import forms
from .models import Booking,Club,Screen,Show
from .models.film import reg

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

class bookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            "seat_number",
            "ticket_type",
            "quantity",
            "card_number",
        ]


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


# class filmForm(forms.ModelForm):
#     class Meta:
#         model = Film
#         fields = [
#             "film_title",
#             "age_rating",
#             "description",
#         ]


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




class regForm(forms.ModelForm):
    class Meta:
        model = reg
        fields = ['email', 'name', 'mobile', 'age', 'seats']
        labels = {
            'email': 'Email',
            'name': 'Name',
            'mobile': 'Mobile Number',
            'age': 'Age',
            'seats': 'Number of Seats'
        }
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile': forms.NumberInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'seats': forms.NumberInput(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-6 mb-0'),
                Column('email', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('mobile', css_class='form-group col-md-6 mb-0'),
                Column('age', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('seats', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Submit')
        )