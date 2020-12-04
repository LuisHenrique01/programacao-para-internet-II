from django.db import models

# Create your models here.

class Game(models.Model):
    """Model definition for Game."""

    created = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=200, blank=True, default='')
    release_date = models.DateField()
    game_category = models.CharField(max_length=200, blank=True, default='')
    played = models.BooleanField(default=False)

    class Meta:
        """Meta definition for Game."""
        ordering = ('name', )
        verbose_name = 'Game'
        verbose_name_plural = 'Games'

    def __str__(self):
        """Unicode representation of Game."""
        return f'{self.name}' # TODO
