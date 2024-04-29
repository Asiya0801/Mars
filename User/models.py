from django.db import models

# Create your models here.
class Apps(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    def str(self) -> str:
        return self.first_name
    
class Product(models.Model):
    name = models.CharField(max_length=255)
    categ = (
        ('Khimars for women and teenage girls.', 'Khimars for women and teenage girls.'),
        ('Abayas for women and teenage girls.', 'Abayas for women and teenage girls.'),
        ('Perfumes for women and teenage girls.', 'Perfumes for women and teenage girls.'),
    )
    category = models.CharField(max_length=255, choices=categ)
    price = models.IntegerField()
    image = models.ImageField(upload_to='images/')
    about = models.TextField()

    def str(self):
        return self.name