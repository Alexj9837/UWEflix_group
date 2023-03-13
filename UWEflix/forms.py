from django import forms
from .models import Booking,Club,Film,Screen,Show

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
            "clubID",
        ]


class filmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = [
            "film_title",
            "age_rating",
            "description",
            "duration",

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
            "date",
            "time",
            "film"
        ]