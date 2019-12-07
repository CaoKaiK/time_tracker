from django.contrib import admin

from .models import User, Contract, Activity, Tag

admin.site.register(Activity)
admin.site.register(Tag)
admin.site.register(User)
admin.site.register(Contract)
