from django.db import models


class Author(models.Model):
    """Model definition for AuthorsModel."""

    class Meta:
        """Meta definition for AuthorsModel."""

        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    LEVELS = (
        ('J', 'Junior developer'),
        ('M', 'Middle developer'),
        ('S', 'Senior developer'),

    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, null=True)
    level = models.CharField(max_length=1, choices=LEVELS)

    def __str__(self):
        """Unicode representation of AuthorsModel."""
        return f'{self.first_name} {self.last_name}'
