from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=False, null=True, default = '')
    address = models.CharField(max_length=150, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    image = models.ImageField(upload_to='profile/',blank=True, null=True)    
    

    def __str__(self):
        return "{0} {1}".format(self.user.first_name,self.user.last_name)

#run when any new institute created or deleted
class Owner(models.Model):
    type = models.CharField(max_length=50, blank=True, null=True)
    institute_id = models.CharField(max_length=50, blank=True, null=True)
    created_by = models.CharField(max_length=30, blank=True, null=True)
    def __str__(self):
        return self.institute_id



class Chain(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=300, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    reg_date = models.DateField(blank=True, null=True)
    currency = models.CharField(max_length=50, blank=True, null=True)
    Bank = models.CharField(max_length=20, blank=True, null=True)
    ifsc = models.CharField(max_length=20, blank=True, null=True)
    commision = models.IntegerField(default=0)
    logo = models.ImageField(upload_to='logo/', blank=True, null=True)
    created_by = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.name

class School(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=300, blank=True, null=True)
    session_start_month = models.CharField(max_length=10, blank=True, null=True)
    session_end_month = models.CharField(max_length=10, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    reg_date = models.DateField(blank=True, null=True)
    currency = models.CharField(max_length=50, blank=True, null=True)
    Bank = models.CharField(max_length=20, blank=True, null=True)
    ifsc = models.CharField(max_length=20, blank=True, null=True)
    logo = models.ImageField(upload_to='logo/', blank=True, null=True)
    front_end = models.BooleanField(default=True, null=True)
    chain = models.ForeignKey(Chain, on_delete=models.CASCADE)
    created_by = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.name

class RolePersission(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    role = models.CharField(max_length=50)
    module = models.CharField(max_length=50)
    create = models.BooleanField(default=False)
    read = models.BooleanField(default=True)
    update = models.BooleanField(default=False)
    delete = models.BooleanField(default=False)
    type = models.CharField(max_length=50, default='tree')
    created_by = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.role


class ProfileRole(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    role = models.ForeignKey(RolePersission, on_delete=models.CASCADE)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    created_by = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.user.phone



