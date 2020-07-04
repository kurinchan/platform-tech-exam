from django.db import models


class Blog(models.Model):
    blog_title = models.CharField(max_length=200)
    blog_content = models.TextField()
    blog_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.blog_title

class Code(models.Model):
    code_title = models.CharField(max_length=200)
    code_content = models.TextField()
    code_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code_title
