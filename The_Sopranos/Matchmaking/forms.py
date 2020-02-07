from django import forms

class statusform(forms.ModelForm):

    class Meta:
        model = Status
        fields = ('fullname','yourpost')

    def __init__(self, *args, **kwargs):
        super(statusform,self).__init__(*args, **kwargs)
        