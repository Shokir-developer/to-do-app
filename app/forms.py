from django import forms
from .models import ToDoApp

class FormToDo(forms.ModelForm):
	class Meta:
		model = ToDoApp
		fields = '__all__'