from django.db import models
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
from pygments.styles import get_all_styles
from django.contrib.auth.models import User
# Create your models here.

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGES_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLES_CHOICES = sorted((item, item) for item in get_all_styles())

class Snippet(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGES_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLES_CHOICES, default='friendly', max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, related_name='snippets', on_delete=models.CASCADE)
    highlighted = models.TextField()


    class Meta:
        ordering = ('created',)

    def save(self, *args, **kwargs):
        """
        Use the pygments library to create a highlighted HTML
        representation of the code snippet.
        """
        lexer = get_lexer_by_name(self.language)
        linenos =self.linenos and 'table' or False
        options = self.title and {'title': self.title} or {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos, full=True, **options)
        self.highlighted=highlight(self.code, lexer, formatter)
        super(Snippet,self).save(*args, **kwargs)
