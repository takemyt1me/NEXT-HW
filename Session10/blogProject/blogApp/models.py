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
    

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete = models.CASCADE, related_name='comments')
    content = models.TextField()

    def __str__(self):
        return self.content



class Recomment(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name = 'recomments')
    content = models.TextField()

    def __str__(self):
        return self.content