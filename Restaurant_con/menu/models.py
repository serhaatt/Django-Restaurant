from django.db import models

    
class Category(models.Model):
    name = models.CharField(max_length=10,null=True)
    def __str__(self):
        return self.name

class Dish(models.Model):
    Food_Name = models.CharField(max_length=30,null=True,verbose_name="Yemek Adı")
    Food_Price = models.PositiveIntegerField(null=True,verbose_name="Yemek Fiyatı")
    Food_Recipe = models.TextField(max_length=1000,null=True,verbose_name="Yemek Tarifi")
    Food_Image = models.ImageField(upload_to="menu/%Y/%m/%d/", default="menu/default.jpeg",verbose_name="Yemek Resmi")
    Food_Available = models.BooleanField(default=True,verbose_name="Aktif")
    Food_Category = models.ForeignKey(Category,null=True,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.Food_Name

