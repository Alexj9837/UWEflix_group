from django import forms
from .models import Booking,Club,Screen,Show
from .models.booking import Booking

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column


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




