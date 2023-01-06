from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.

class Products(models.Model):
    name=models.CharField(max_length=200)
    price=models.PositiveIntegerField()
    description=models.CharField(max_length=200)
    category=models.CharField(max_length=200)
    image=models.ImageField(null=True,upload_to="images")

    @property
    def avg_rating(self):
        ratings=self.reviews_set.all().values_list("rating",flat=True)
        if ratings:
            return sum(ratings)/len(ratings)
        else:
            return 0

    def review_user(self):
        ratings=self.reviews_set.all().values_list("rating",flat=True)
        if ratings:
            return len(ratings)
        else:
            return 0

    def __str__(self):
        return self.name

#ORM
#modelname.objects.create(field1=value1,field2=value2,,,,)
#Products.objects.create(name="samsunga72",price=32000,description="mobile",category="electronics")

#orm query for fetching all records
#qs=modelname.objects.all()

class Carts(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)


class Reviews(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    rating=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    comment=models.CharField(max_length=200)

    def __str__(self):
        return self.comment
