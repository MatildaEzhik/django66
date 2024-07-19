from django.db import models

# Create your models here.
class Platform(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    genre = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    release_date = models.DateField()
    platforms = models.ManyToManyField(Platform)
    image = models.ImageField(upload_to='game_images/')

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    purchases = models.ManyToManyField(Game)

    def __str__(self):
        return self.user.username
