
from .validators import validate_login, validate_email
from django.db import models
import datetime

# Create your models here.
class User(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    login = models.TextField(validators=[validate_login])
    email = models.TextField(validators= [validate_email])


    def __str__(self) -> str:
        return f'first Name:{self.first_name}, second Name: {self.last_name}'
class Category(models.Model):
    name = models.TextField()
    
    def __str__(self):
        return f"{self.name}"


class Post(models.Model):
    title = models.TextField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    now = datetime.datetime.now()
    def __str__(self) -> str:
        return f"Post:{self.title}, datecreated: {self.now.date()}, category: {self.category_id}" 