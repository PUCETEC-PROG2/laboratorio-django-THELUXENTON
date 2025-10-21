from django.db import models

class Pokemon(models.Model):
    name = models.CharField(max_length=30, null=False)
    type = models.CharField(max_length=30, null=False)
    weight = models.DecimalField(decimal_places=4, max_digits=6)
    height = models.DecimalField(decimal_places=4, max_digits=6)
    
    def __str__(self):
        return self.name

class Trainer(models.Model):
    first_name = models.CharField(max_length=50)       
    last_name = models.CharField(max_length=50)        
    age = models.PositiveIntegerField()          
    date_of_birth = models.DateField()       
    level = models.PositiveIntegerField()          
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
