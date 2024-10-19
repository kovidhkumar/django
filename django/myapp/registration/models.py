from django.db import models

class Registration(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()  # Date of Birth
    doj = models.DateField()  # Date of Joining
    role = models.CharField(max_length=100)
    password = models.CharField(max_length=100)  # You can use hashing for passwords later
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)  # Phone numbers can have different formats, so CharField is fine

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
