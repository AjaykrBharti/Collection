from django.db import models


class UploadImage(models.Model):
    name = models.CharField(max_length=40,null=False,default=False)
    image = models.ImageField(default=False,null=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.created_date)


# Create your models here.
