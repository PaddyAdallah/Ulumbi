from django.db import models


class Employee(models.Model):
    empName = models.TextField()
    empPhoto = models.ImageField(upload_to='Emp Photo', blank=True)
    empDescription = models.TextField()

    def __str__(self):
        return self.empDescription + self.empName
