from django.contrib import admin
from .models import UploadedImage, Places


# Register your models here.
admin.site.register(UploadedImage)
admin.site.register(Places)