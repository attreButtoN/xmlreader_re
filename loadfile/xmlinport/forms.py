from django import forms


class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label="Выберите файлы",
        help_text="максимальный вес 42 мегабайта",
        widget=forms.FileInput(attrs={"multiple": True}),
    )


class XmlForm(forms.Form):
    xmlfile = forms.FileField(
        label="Выберите файлы",
        help_text="максимальный вес 42 мегабайта",
        widget=forms.FileInput(attrs={"multiple": True}),
    )
