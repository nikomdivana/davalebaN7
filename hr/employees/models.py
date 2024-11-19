from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    salary = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
