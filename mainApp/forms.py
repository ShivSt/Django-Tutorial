from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Tutorial, TutorialSeries, TutorialCategory
from tinymce.widgets import TinyMCE

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class TutorialForm(forms.ModelForm):    # We extends forms.Form for custom form
    tutorial_slug = forms.CharField(help_text="slug is a unique identifier for the tutorial")
    tutorial_content = forms.CharField(widget=TinyMCE(mce_attrs={'width': 100})
     )

    class Meta:
        model = Tutorial
        fields = ("tutorial_title", "tutorial_series", "tutorial_slug", "tutorial_content")
        
    """ using forms.Form
    #all_series = [s.tutorial_series for s in TutorialSeries.objects.all()]
    SERIES_CHOICES = [(obj.tutorial_series , obj) for obj in TutorialSeries.objects.all()]
    title = forms.CharField()
    linked_series = forms.ChoiceField(choices=SERIES_CHOICES)
    content = forms.CharField(widget=forms.Textarea )
    slug= forms.CharField()

    class Meta:
        model = Tutorial
        fields = ("tutorial_title", "tutorial_series", "tutorial_slug", "tutorial_content")

    def save(self, commit=True):
        
        tutorial = Tutorial()   #super(TutorialForm, self).save(commit=False)
        tutorial.tutorial_title = self.cleaned_data["title"]
        tutorial.tutorial_series = self.cleaned_data["linked_series"] 
        tutorial.tutorial_content = self.cleaned_data["content"]
        tutorial.tutorial_slug = self.cleaned_data["slug"]
        if commit:
            tutorial.save()
        return tutorial
    """

class TutorialCategoryForm(forms.ModelForm):
    category_slug = forms.CharField(help_text="slug is a unique identifier for the category. It will be used for category url")

    class Meta:
        model = TutorialCategory
        fields = '__all__'


class TutorialSeriesForm(forms.ModelForm):

    class Meta:
        model = TutorialSeries
        fields = '__all__'