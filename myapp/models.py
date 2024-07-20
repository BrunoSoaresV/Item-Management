from django.db import models

class Item(models.Model):
    nome = models.CharField(max_length=100)
    descrição = models.TextField()
    preço= models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'item'
