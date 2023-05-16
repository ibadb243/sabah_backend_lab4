from django.db import models

# Create your models here.
class Account(models.Model):
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    about = models.TextField()
    profile_image = models.ImageField()

    def __str__(self) -> str:
        return f"{self.name} {self.surname}"

class Article(models.Model):
    title = models.CharField(max_length=256)
    author = models.ForeignKey(Account, on_delete=models.DO_NOTHING)
    content = models.TextField()
    published = models.DateTimeField()

    def __str__(self) -> str:
        return f"{self.title}"