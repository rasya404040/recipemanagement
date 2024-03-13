from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=30)
    type = models.CharField(max_length=45)
    ingredients=models.TextField()
    desc = models.TextField()
    image = models.ImageField(upload_to="images/recipe", null=True, blank=True)

    def __str__(self):
        return self.title

class Review(models.Model):
    recipe=models.ForeignKey(Recipe,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review=models.TextField()
    rating=models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.review
