from django.db import models

class Comment(models.Model):
    name = models.CharField(max_length=30,blank=True)
    email = models.EmailField(max_length=40,blank=True)
    image = models.ImageField(upload_to="comments/%Y/%m/%d/", default="comments/2024/07/18/default.jpg",verbose_name="Müşteri Resmi",blank=True,null=True)
    message = models.TextField(max_length=300,blank=False)
    def __str__(self):
        return self.email
