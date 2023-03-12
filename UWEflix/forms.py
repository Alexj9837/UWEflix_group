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
        ]

class ClubRegistrationForm(forms.Form):
    name = forms.CharField(label='Club name', max_length=255)
    address = forms.CharField(label='Address', max_length=255,
        widget=forms.TextInput(attrs={'placeholder': 'Street, City, Postcode'})
    )
    contact_details = forms.CharField(label='Contact details', max_length=255)
    first_name = forms.CharField(label='First name', max_length=255)
    last_name = forms.CharField(label='Last name', max_length=255)
    date_of_birth = forms.DateField(label='Date of birth', widget=forms.SelectDateWidget(years=range(1900, 2020)))
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
