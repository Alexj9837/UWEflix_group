from django import forms
from . import models

class bookingForm(forms.ModelForm):
    class Meta:
        model = models.booking
        fields = [
            "seat_number",
            "ticket_type",
            "quantity",
            "card_number",
        ]


class ClubForm(forms.ModelForm):
    class Meta:
        model = models.Club
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
        model = models.film
        fields = [
            "film_title",
            "age_rating",
            "description",
        ]


class screenForm(forms.ModelForm):
    class Meta:
        model = models.screen
        fields = [
            "screen_number",
        ]


class showForm(forms.ModelForm):
    class Meta:
        model = models.show
        fields = [
            "date",
            "time",
        ]