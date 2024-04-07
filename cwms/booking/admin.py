from django.contrib import admin
from .models import CarWashBooking
# Register your models here.


class CarWashBookingAdmin(admin.ModelAdmin):
    list_display = ['bookingId' , 'name' , 'packageType' ,
                     'carwashpoint' , 'washdate' , 'postingDate']
    
admin.site.register(CarWashBooking , CarWashBookingAdmin)