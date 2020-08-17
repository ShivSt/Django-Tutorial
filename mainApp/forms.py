from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Tutorial, TutorialSeries, TutorialCategory

"""
class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2",)

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
"""

class TutorialForm(forms.Form):    # We extends forms.ModelForm for easy form
    """
    tutorial_slug = forms.CharField(help_text="slug is a unique identifier for the tutorial")
    tutorial_content = forms.CharField(widget=TinyMCE(mce_attrs={'width': 100})
     )

    class Meta:
        model = Tutorial
        fields = ("tutorial_title", "tutorial_series", "tutorial_slug", "tutorial_content")
        
    """ 
    
    SERIES_CHOICES = [(obj , obj) for obj in TutorialSeries.objects.all()]
    title = forms.CharField()
    linked_series = forms.ChoiceField(choices=SERIES_CHOICES)
    content = forms.CharField()
    slug= forms.CharField(help_text='slug is a unique identifier for this tutorial')

    class Meta:
        model = Tutorial
        fields = ("tutorial_title", "tutorial_series", "tutorial_slug", "tutorial_content")


    def save(self, commit=True):
        
        tutorial = Tutorial()  #super(TutorialForm, self)
        tutorial.tutorial_title = self.cleaned_data["title"]
        # this filtering is needed because the choiceField is returning string and we need object
        tutorial.tutorial_series = TutorialSeries.objects.filter(tutorial_series = self.cleaned_data['linked_series'])[0]
        tutorial.tutorial_content = self.cleaned_data["content"]
        tutorial.tutorial_slug = self.cleaned_data["slug"]
        if commit:
            tutorial.save()
        return tutorial
    

class TutorialCategoryForm(forms.ModelForm):
    category_slug = forms.CharField(help_text="slug is a unique identifier for the category. It will be used for category url")

    class Meta:
        model = TutorialCategory
        fields = '__all__'


class TutorialSeriesForm(forms.ModelForm):

    class Meta:
        model = TutorialSeries
        fields = '__all__'