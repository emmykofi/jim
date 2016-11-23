from itertools import chain

from django.shortcuts import get_object_or_404, render

from . import models


def flight_list(request):
	bookings = models.Booking.objects.all()
	return render(request, 'bookings/flight_list.html', {'bookings': bookings})


def booking_detail(request, pk):
	booking = get_object_or_404(models.Booking, pk=pk)
	return render(request, 'bookings/booking_detail.html', {'booking': booking})


def text_detail(request, booking_pk, step_pk):
	step = get_object_or_404(models.Text,booking_id=booking_pk, pk=step_pk)
	return render (request, 'bookings/step_detail.html', {'step': step})

