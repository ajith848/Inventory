from django.db import models
from django.contrib.auth.models import AbstractUser, Group,Permission

# Create your models here.
class User(AbstractUser):
    # username=models.CharField(max_length=50)
    email = models.EmailField(unique=True)


    def __str__(self):
        return self.username
   
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_groups',  # Set custom related_name
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',  # Set custom related_name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )


class Inventory(models.Model):
    product_id = models.CharField(max_length=50, unique=True)
    product_name= models.CharField(max_length=200)
    Category = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    quantity= models.IntegerField(default=0)
    price =models.DecimalField(max_digits=10, decimal_places=2)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.product_name} ({self.product_id})"
