from django import forms  
class StudentForm(forms.Form):  
    choice = (
    ("1", "Same template"),
    ("2", "Whatsapp template"),
)
    file  = forms.FileField() # for creating file input  
    choice = forms.ChoiceField(choices = choice)