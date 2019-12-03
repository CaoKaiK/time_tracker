from django.contrib import admin
from .models import Customer, Group, Element, Entry, Day

admin.site.register(Customer)
admin.site.register(Group)
admin.site.register(Element)
admin.site.register(Entry)
admin.site.register(Day)
