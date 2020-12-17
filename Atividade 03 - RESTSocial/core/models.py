from django.db import models
# Create your models here.

class Profile(models.Model):
    """Model definition for MODELNAME."""

    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=254)
    address = models.JSONField()

    def total_posts(self):
        total_posts = Post.objects.filter(userId=self).count()
        return total_posts
    
    def total_comments(self):
        total_comments = Comment.objects.filter(postId__userId=self).count()
        return total_comments
        
    class Meta:
        """Meta definition for MODELNAME."""

        verbose_name = 'Profile'
        verbose_name_plural = 'Profile'

    def __str__(self):
        """Unicode representation of MODELNAME."""
        return '%s'%self.name
    
    
class Post(models.Model):
    """Model definition for Post."""

    title = models.TextField()
    body = models.TextField()
    userId = models.ForeignKey(Profile, related_name='posts', on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Post."""

        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        """Unicode representation of Post."""
        return f'{self.title}' # TODO


class Comment(models.Model):
    """Model definition for Comment."""

    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=254)
    body = models.TextField()
    postId = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Comment."""

        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        """Unicode representation of Comment."""
        return '{}'.format(self.body) # TODO

