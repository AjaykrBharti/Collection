from django.db import models


class accounts(models.Model):
    GENDER_CHOICES = [
        ('F', 'Female'),
        ('M', 'Male'),
    ]
    COMPANY_CHOICES = [
        ('Tata','Tata'),
        ('EEEHUB','EEEHUB'),
        ('ISRO','ISRO'),
    ]
    LOCATION_CHOICES = [
        ('Katihar', 'Katihar'),
        ('Patna','Patna'),
        ('Mumbai','Mumbai'),
    ]
    EmpName = models.CharField(max_length=40, null=True)
    EmpComp = models.CharField(choices=COMPANY_CHOICES, max_length=10, null = True)
    EmpGender = models.CharField(choices=GENDER_CHOICES, max_length=6, null=True)
    EmpSalary = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    EmpLocation = models.CharField(choices=LOCATION_CHOICES,max_length=10,null=True)
    EmpEmail = models.EmailField(max_length=254,null=True)

    def __str__(self):
        return self.EmpName





# Create your models here.
