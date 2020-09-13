from django.contrib import admin

from profiles_api import models # Import models.py from our app

# Register your models here.
admin.site.register(models.UserProfile) # After register, this model will show up on admin interface
admin.site.register(models.ProfileFeedItem)
