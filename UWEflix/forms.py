from django import forms
from .models import Booking,Club,Film,Screen,Show

# forms page has the fields that we will be using for each of our models, 
# this allows us to take in information from the webpage i.e "seat_number"

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


class filmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = [
            "film_title",
            "age_rating",
            "description",
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
            "screen",
            1
        ]
        
        