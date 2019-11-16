from django.contrib import admin
from .models import Project, Element, Entry, Account, Day

admin.site.register(Project)
admin.site.register(Element)
admin.site.register(Entry)

admin.site.register(Account)
admin.site.register(Day)
