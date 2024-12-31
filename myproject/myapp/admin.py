from django.contrib import admin
from .models import Tour
from .models import Contact  # Import the Contact model

# Register your models here.
admin.site.register(Tour)

# Register the model with Django's admin site
admin.site.register(Contact)
