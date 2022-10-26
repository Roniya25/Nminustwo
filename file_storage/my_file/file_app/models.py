from django.db import models

# Create your models here.
class Personal(models.Model):
    Name = models.CharField(max_length=25)
    Description = models.TextField()
    Upload_file = models.FileField(upload_to='self/pdf/')

    def __str__(self):
        return self.Name
