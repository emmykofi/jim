from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from . import forms


def home_page(request):
	return render(request, 'home.html')

def flight_view(request):
	form = forms.FlightForm()
	if request.method == 'POST':
		form = forms.FlightForm(request.POST)
		if form.is_valid():
			print("my flights")
	return render(request, 'flight_form.html', {'form': form})



def contact_page(request):
	return render(request, 'contact.html')

