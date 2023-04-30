from django.db import models

# Create your models here.

# class Author(models.Model):
#     Name = models.CharField(max_length=32)
#     Surname = models.CharField(max_length=32)

#     class Meta:
#         verbose_name = "Author"
#         verbose_name_plural = "Authors"

# class Article(models.Model):
#     Title = models.CharField(max_length=64)
#     Author = models.ForeignKey(Author, on_delete=models.CASCADE)
#     Tag = models.CharField(max_length=16)
#     Content = models.TextField()
#     Published = models.TimeField()
#     Views = models.IntegerField()

#     class Meta:
#         verbose_name = "Article"
#         verbose_name_plural = "Articles"

class Author(models.Model):
    Name = models.CharField(max_length=32, verbose_name="Имя")
    Surname = models.CharField(max_length=32, verbose_name="Фамилия")

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"
        
    def __str__(self) -> str:
        return f"{self.Name} {self.Surname}"

class Article(models.Model):
    Title = models.CharField(max_length=64, verbose_name="Заголовок")
    Author = models.ForeignKey(Author, verbose_name="Автор", on_delete=models.DO_NOTHING)
    Tag = models.CharField(max_length=16, verbose_name="Метка")
    Content = models.TextField(verbose_name="Содержимое")
    Published = models.DateTimeField(verbose_name="Дата Публикации")
    Views = models.IntegerField(verbose_name="Количество Просмотров", default=0)

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
    
    def __str__(self) -> str:
        return f"{self.Title}, опубликованно {self.Published} {self.Views}"