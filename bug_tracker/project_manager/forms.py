from django.forms import ModelForm

from .models import Project, Client


class ProjectAddForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'