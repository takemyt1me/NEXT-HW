from django.db import models
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    def article_count(self):
        return self.article_set.count()
    
class Article(models.Model):
    title = models.CharField(max_length = 200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title