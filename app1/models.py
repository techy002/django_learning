from django.db import models

# Create your models here.
class UserProfile(models.Model):
    name = models.CharField(max_length=150, null=True,blank=True)
    addres = models.TextField(max_length=500, null=True,blank=True)
    mobile = models.IntegerField(default=1234567890)

    def __str__(self):
        return str(self.id)
    
class BusinessProfile(models.Model):
    user = models.ForeignKey(UserProfile,on_delete = models.CASCADE,null=True,blank=True)
    addres = models.TextField(max_length=500, null=True,blank=True)
    mobile = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return str(self.id)
    