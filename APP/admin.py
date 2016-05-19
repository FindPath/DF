from django.contrib import admin

# Register your models here.
from APP.models import *

admin.site.register(Tag)
admin.site.register(Question)
admin.site.register(Answer)