from django.db import models


class Author(models.Model):
    user = models.OneToOneField("User", on_delete = models.CASCADE)
    rating_author = models.IntegerField(default = 0)

    def update_rating(self):
        pass

class Category(models.Model):
    name = models.CharField(max_length = 255, unique = True)

class Post(models.Model):
    author = models.OneToOneField("Author", on_delete = models.CASCADE)
    tipe = models.BooleanField()
    date = models.DateTimeField(auto_now_add = True)
    category = models.ManyToMany("Category", through = 'PostCategory')
    header = models.CharField(max_length = 124)
    text = models.CharField(max_length = 255)
    rating_post = models.IntegerField(default = 0)

    def like(self):
        pass
    def dislike(self):
        pass
    def preview(self):
        pass

class PostCategory(models.Model):
    post = models.ForeignKey("Post", on_delete = models.CASCADE)
    category = models.ForeignKey("Category", on_delete = models.CASCADE)

class Comment(models.Model):
    post = models.ForeignKey("Post", on_delete = models.CASCADE)
    user = models.ForeignKey("User", on_delete = models.CASCADE)
    text = models.CharField(max_length = 500)
    date = models.DateTimeField(auto_now_add = True)
    rating = models.IntegerField(default = 0)

    def like(self):
        pass
    def dislike(self):
        pass
# Create your models here.
