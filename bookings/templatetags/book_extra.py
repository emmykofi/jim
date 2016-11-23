from django import template
from django.utils.safestring import mark_safe

import markdown2

from bookings.models import Booking

register = template.Library()


@register.inclusion_tag('bookings/booking_nav.html')
def nav_booking_list():
	'''Returns dictionary of courses to display as navigation pane'''
	bookings = Booking.objects.all()
	return{'bookings': bookings}


@register.filter('markdown_to_html')
def markdown_to_html(markdown_text):
	'''converts markdown text to html'''
	html_body = markdown2.markdown(markdown_text)
	return mark_safe(html_body)

