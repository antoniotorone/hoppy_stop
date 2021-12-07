from django.db import models


class ProductSuggestion(models.Model):
    name = models.CharField(max_length=254)
    comment = models.TextField(max_length=1000)
    style = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name
