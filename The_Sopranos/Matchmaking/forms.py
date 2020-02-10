from django import forms
from .models import Status


class statusform(forms.ModelForm):

    class Meta:
        model = Status
        fields = ('fullname','yourpost',)

    def __init__(self, *args, **kwargs):
        super(statusform,self).__init__(*args, **kwargs)
        