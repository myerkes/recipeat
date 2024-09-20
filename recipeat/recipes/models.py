from django.db import models

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=255)
    yields = models.CharField(max_length=255)
    total_time = models.IntegerField()
    image = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    
class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    comment = models.TextField()
    name = models.CharField(max_length=255)
    preparation = models.CharField(max_length=255)
    purpose = models.CharField(max_length=255)
    quantity = models.DecimalField(decimal_places=3,max_digits=7)
    quantity_max = models.DecimalField(decimal_places=3,max_digits=7)
    sentence = models.TextField()
    size = models.CharField(max_length=255)
    unit = models.CharField(max_length=255)
    unit_text = models.CharField(max_length=255)

class Instruction(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    step = models.IntegerField()
    text = models.TextField()
