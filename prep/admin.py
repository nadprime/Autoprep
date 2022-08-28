from django.contrib import admin
from prep.models import Contact

from . models import myuploadfile



admin.site.register(myuploadfile)


# Register your models here.
admin.site.register(Contact)
