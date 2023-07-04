from django.db import models

class Organizer(models.Model):
    name =  models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    date_of_registration = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
