from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    rating_author = models.IntegerField(default = 0)

    def update_rating(self):
        author_articles_rating = self.post_set.all().aggregate(post_rating = Sum('post_rating'))
        author_comments_rating = self.user.comment_set.all().aggregate(comment_rating = Sum('comment_rating'))
        comments_to_author_articles_rating = Comment.objects.filter(post_author = self.id)
        return author_articles_rating * 3 + author_comments_rating + comments_to_author_articles_rating

class Category(models.Model):
    culture = 'CU'
    science = 'SC'
    tech = 'TE'
    politics = 'PO'
    sport = 'SP'
    entertainment = 'EN'
    economics = 'EC'
    education = 'ED'

    CATEGORIES = [
        (culture, 'Культура'),
        (science, 'Наука'),
        (politics, 'Политика'),
        (sport, 'Спорт'),
        (economics, 'Экономика'),
        (education, 'Развлечения'),
        (tech, 'Технологии'),
        (entertainment, 'Образование')
    ]

    name = models.CharField(max_length = 2, unique = True, choices = CATEGORIES)

class Post(models.Model):
    article = 'AR'
    news = 'NE'

    POST_TYPES = [
        (article, 'Статья'),
        (news, 'Новость')
    ]

    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    post_type = models.CharField(max_length = 2, choices = POST_TYPES)
    date = models.DateTimeField(auto_now_add = True)
    post_category = models.ManyToManyField(Category, through = 'PostCategory')
    header = models.CharField(max_length = 124)
    text = models.TextField()
    post_rating = models.IntegerField(default = 0)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def like(self):
        self.likes += 1
        self.save()

    def dislike(self):
        self.dislikes -= 1
        self.save()

    def preview(self):
        return f'{self.text[0:124]}...'

class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    comment_rating = models.IntegerField(default = 0)

    def like(self):
        self.likes += 1
        self.save()

    def dislike(self):
        self.dislikes -= 1
        self.save()
# Create your models here.
