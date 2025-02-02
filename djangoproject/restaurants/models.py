from django.conf import settings
from django.db import models
from datetime import datetime
from .utils import unique_slug_generator
from django.db.models.signals import pre_save
from .validators import validate_category
from django.urls import reverse

# Create your models here.
User = settings.AUTH_USER_MODEL
class RestaurantLocation(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=120)
	location = models.CharField(max_length=120, null=True, blank=True)
	category = models.CharField(max_length=120, null=True, blank=True, validators=[validate_category])
	timestamp= models.DateTimeField(default=datetime.now,blank=True)
	slug = models.SlugField(null=True, blank=True)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('restaurants:detail', kwargs= { 'slug': self.slug })
	@property
	def title(self):
		return self.name

def rl_pre_save_reciever(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug= unique_slug_generator(instance)

pre_save.connect(rl_pre_save_reciever, sender=RestaurantLocation)