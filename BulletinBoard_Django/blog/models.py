from django.db import models
from django.contrib.auth.models import User, AbstractUser, UserManager
from django.utils import timezone


# class CustomUser(AbstractUser):
#     class Meta:
#         app_label = 'app'
#         profile_picture = models.ImageField(upload_to='profiles')
#
#         objects = UserManager()
#
#         def __unicode__(self):
#             return self.username


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    favorite_num = models.IntegerField(default=0)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    # def approved_comments(self):
    #     return self.comments.filter(approved_comment=True)


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_user')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    # def approve(self):
    #     self.approved_comment = True
    #     self.save()

    def __str__(self):
        return self.text


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorite_user')
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} like \'{self.post.title}\''

