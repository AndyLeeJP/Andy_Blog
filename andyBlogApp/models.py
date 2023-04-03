from django.db import models
from markdownx.models import MarkdownxField

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 255)
    slug = models.SlugField()
    intro = models.TextField()
    body = MarkdownxField()
    posted_date = models.DateTimeField(auto_now_add=True)





