from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Profile(models.Model):
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=False, null=True, default = '')
    address = models.CharField(max_length=150, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    image = models.ImageField(upload_to='media/profile/',blank=True, null=True)    
    

    def __str__(self):
        return self.phone



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

class ChainRole(models.Model):
    chain = models.ForeignKey(Chain, on_delete=models.CASCADE)
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

class SchoolRole(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
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


class SchoolProfileRole(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    role = models.ForeignKey(SchoolRole, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    created_by = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.user.phone

class ChainProfileRole(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    role = models.ForeignKey(ChainRole, on_delete=models.CASCADE)
    chain = models.ForeignKey(Chain, on_delete=models.CASCADE)
    created_by = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.user.phone


