from django import forms
from .models import Person

class ExcelForm(forms.Form):
    name = forms.ChoiceField(choices=[])

    def __init__(self, *args, **kwargs):
        choices = kwargs.pop('choices', [])
        super().__init__(*args, **kwargs)
        self.fields['name'].choices = choices
        
        
class UploadExcelForm(forms.Form):
    excel_file = forms.FileField()


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        exclude = ['ari8mosEisagoghs']
        widgets = {
            'titlos': forms.Textarea(attrs={
                'rows': 1,
            }),
            'syggrafeas': forms.Textarea(attrs={
                'rows': 1,
            }),
            'troposPromPar': forms.Textarea(attrs={
                'rows': 1,
            }),
            'ekdoths': forms.Textarea(attrs={
                'rows': 1,
            }),
            'koha': forms.Textarea(attrs={
                'rows': 1,
            }),
        }
