

from django import forms


from tasks.models import Tasks

from tasks.models import Tag


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=255)
    message = forms.CharField(max_length=65536,widget=forms.Textarea)
    sender = forms.EmailField()


class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['content','deadline','tags']
        widgets = {
            'deadline' : forms.DateTimeInput( attrs = {'type' : 'datetime-local'})
        }

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'

