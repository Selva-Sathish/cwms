from django.db import models

# Create your models here.

class CarWashBooking(models.Model):
    bookingId = models.CharField(max_length= 20 )
    packageType = models.IntegerField()
    carwashpoint = models.IntegerField()
    name = models.CharField(max_length=100)
    washdate = models.DateField()
    washtime = models.CharField(max_length=50)
    message = models.CharField(max_length=100)
    status = models.CharField(max_length= 30)
    adminremark = models.CharField(max_length=50)
    paymentmode = models.CharField(max_length= 100)
    postingDate = models.DateField()
    updateDate = models.DateField()