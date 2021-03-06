from django import forms

from post.models import Question
from post.models import Channel


class post_form(forms.ModelForm):
    channels = forms.ModelChoiceField(queryset=Channel.objects.filter(visible=True).order_by('name'), required=False)

    class Meta:
        model = Question
        fields = ('title', 'description', 'channels')

    def __init__(self, *args, **kwargs):
        super(post_form, self).__init__(*args, **kwargs)
        self.fields["channels"].choices = [("", ""), ] + list(self.fields["channels"].choices)[1:]
