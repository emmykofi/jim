from django.core.urlresolvers import reverse
from django.db import models


class Booking(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=255)
	description = models.TextField()


	def __str__(self):
		return self.title


class Step(models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField()
	order = models.IntegerField(default=0)
	booking = models.ForeignKey(Booking)

	class Meta:
		abstract = True
		ordering = ['order',]


	def __str__(self):
		return self.title


class Text(Step):
	content = models.TextField(blank=True, default='')

	def get_absolute_url(self):
		return reverse('booking:text', kwargs={
					'booking_pk': self.booking_id,
					'step_pk': self.id
			})



