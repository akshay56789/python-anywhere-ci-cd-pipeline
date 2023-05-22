from django.contrib import admin
from home.models import Fare, Kochi_fare, Jaipur_fare, Nagpur_fare

admin.site.register(Fare)
admin.site.register(Kochi_fare)
admin.site.register(Jaipur_fare)
admin.site.register(Nagpur_fare)