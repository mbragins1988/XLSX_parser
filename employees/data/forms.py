from django import forms

from data.models import Data


class AddFileForm(forms.ModelForm):
    """Класс формы добавления файла."""

    class Meta:
        """Мета-класс."""

        model = Data
        fields = ['familija', 'imja']
