from django.db import models

# Create your models here.

class Textbooks(models.Model):
    name = models.CharField(max_length=255, null=False)
    author = models.CharField(max_length=255, null=False)
    condition = models.CharField(max_length=255, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, default = 0)
    def __str__(self):
        return "{} - {} - {}".format(self.name, self.author, self.condition, self.price)

