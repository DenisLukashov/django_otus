from django import forms
from authors.models import Author


class AuthorForm(forms.ModelForm):
    """AuthorForm definition."""

    class Meta:

        model = Author
        # fields = ('first_name', 'last_name', 'email',)
        exclude = ('level',)
