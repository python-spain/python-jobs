from django.forms import ModelForm
from .models import Job
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class JobForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(JobForm, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)

        # You can dynamically adjust your layout
        self.helper.layout.append(Submit('save', 'save'))

    class Meta:
        model = Job
        fields = '__all__'
        exclude = ['created_at', 'published_at', 'times_viewed']
