from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.jpg', blank=True)

    def __str__(self): #defines how the articles are going to look like both in the shell and the admin,,human-readable
        return self.title

    def snippet(self):
        return self.body[:400] + '...'
