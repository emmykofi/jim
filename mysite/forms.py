from django import forms
import datetime
from django.core import validators



CLASS_OF_SERVICE_CHOICES = (
    ('economy ', 'Economy'),
    ('business', 'Business'),
)

FROM_CHOICES = (
    ('harare ', 'Harare'),
    ('bulawayo', 'Bulawayo'),
    ('johansburg', 'Johansburg'),
    ('lusaka', 'Lusaka'),
    ('kariba', 'Kariba'),
)

TO_CHOICES = (
    ('harare ', 'Harare'),
    ('bulawayo', 'Bulawayo'),
    ('johansburg', 'Johansburg'),
    ('lusaka', 'Lusaka'),
    ('kariba', 'Kariba'),
)
Flights_CHOICES = (
    ('round_trip ', 'Round Trip'),
    ('one_way', 'One Way'),
)


class FlightForm(forms.Form):
	flights = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=Flights_CHOICES,
    )
	From = forms.MultipleChoiceField(
        required=False,
        widget=forms. Select,
        choices=FROM_CHOICES,
    )
	TO = forms.MultipleChoiceField(
        required=False,
        widget=forms. Select,
        choices=TO_CHOICES,
    )
	Departure = forms.DateField(widget=forms.SelectDateWidget)
	Return = forms.DateField(widget=forms.SelectDateWidget)
	Adults = forms.IntegerField()
	Children = forms.IntegerField()
	Infants = forms.IntegerField()
	class_of_service = forms.MultipleChoiceField(
        required=False,
        widget=forms. Select,
        choices=CLASS_OF_SERVICE_CHOICES,
    )
	honeypot = forms.CharField(required=False, 
							   widget=forms.HiddenInput, 
							   label="Leave empty",
							   validators=[validators.MaxLengthValidator(0)]
							   )

