from django.db import models

class Size(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Type(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Colour(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Item(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    price = models.DecimalField(decimal_places=2, max_digits=12)
    quantity = models.PositiveIntegerField(default=0)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, default='Top')
    size = models.ForeignKey(Size, on_delete=models.CASCADE, default='M')
    colour = models.ForeignKey(Colour, on_delete=models.CASCADE, default='Blue')

    def __str__(self):
        return f'{self.name} // {self.description} // {self.price} // {self.quantity} // {self.type} // {self.size} // {self.colour}'
