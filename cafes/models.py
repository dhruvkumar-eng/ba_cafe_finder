from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Barrio(models.Model):
    name = models.CharField(max_length=50,unique=True)
    communa = models.IntegerField(
    default=1,
    validators=[MinValueValidator(1), MaxValueValidator(5)]
)

    def __str__(self):
        return f"{self.name} ({self.communa})"


class Cafe(models.Model):      
       
       name = models.CharField(max_length=100)
       address = models.CharField(max_length=200, default="")
       barrio = models.ForeignKey(
          Barrio, null=True, blank=True,
          on_delete=models.PROTECT, related_name='cafes')
       rating = models.IntegerField(
          validators=[MinValueValidator(1), MaxValueValidator(5)]
      )
       has_good_medialunas = models.BooleanField(default=False)

       notes = models.TextField(blank=True)

       
       class Meta:
          ordering = ['-rating', 'name']
       def __str__(self):
        return f"{self.name} ({self.barrio})"
       
class Reviewer(models.Model):
    name = models.CharField(max_length=100)
    join_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.join_date})"





   
   
              
    
