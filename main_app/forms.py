from django.forms import ModelForm

from .models import Timeline

class TimelineForm(ModelForm):
    class Meta:
        model = Timeline
        fields = ['date', 'action']