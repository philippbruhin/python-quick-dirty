from django.db import models
from django.utils.translation import gettext_lazy as _

from translated_fields import TranslatedField

class Question(models.Model):
    question = TranslatedField(
        models.CharField(_("question"), verbose_name="Question Verbose Name", max_length=200),
    )
    answer = TranslatedField(
        models.CharField(_("answer"), verbose_name="Answer Verbose Name", max_length=200),
    )

    def __str__(self):
        return self.question