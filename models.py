from django.db import models
from django.contrib.auth.models import User
class gallery(models.Model):
    title =models.TextField()
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    description=models.TextField()
    image=models.ImageField(upload_to='image/',null=True)
    price=models.DecimalField(max_digits=6, decimal_places=2)
    def __str__(self):
        return self.title
class buy_art(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    art=models.ForeignKey(gallery, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username