from .models import Article
from django.forms import ModelForm, TextInput, DateInput, Textarea


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'Stat', 'full_text', 'date']

        widgets = {
            "title": TextInput(attrs={'class': 'form-control', 'placeholder': 'ФИО'}),
            "Stat": TextInput(attrs={'class': 'form-control', 'placeholder': 'Электронная почта'}),
            "full_text": Textarea(attrs={'class': 'form-control', 'placeholder': 'Текст сообщения'}),
            "date": DateInput(attrs={'class': 'form-control', 'placeholder': 'Дата написания (дд.мм.гг.)'})
}
