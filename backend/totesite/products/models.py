from django.db import models

class ToteBag(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='tote_bags/')
    style = models.CharField(max_length=50)

    def __str__(self):
        return self.name