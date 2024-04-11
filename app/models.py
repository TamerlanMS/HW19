from django.db import models

class IcecreamShop(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def str(self):
        return self.name

class Icecream(models.Model):
    flavor = models.CharField(max_length=100)
    description = models.TextField()
    shop = models.ForeignKey(IcecreamShop, on_delete=models.CASCADE, related_name='icecreams')

    def str(self):
        return self.flavor