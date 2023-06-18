from django.db import models

# Create your models here.
class students(models.Model):
      fname = models.CharField(max_length=100)
      lname = models.CharField(max_length=100)
      email = models.CharField(max_length=100)
      course = models.CharField(max_length=100)
      gender = models.CharField(max_length=100)
      address = models.CharField(max_length=100)
      image=models.ImageField(upload_to="static/images",default="")
      class Meta:
            db_table="students"

      def __str__(self):
            return self.fname