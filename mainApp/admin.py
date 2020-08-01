from django.contrib import admin
from .models import Tutorial, TutorialSeries, TutorialCategory

# for including tinymce widget in our admin editor 
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.

""" Control which fields and how to show them on admin page """
class TutorialAdmin(admin.ModelAdmin):
    """
    #This will display selected fields
    fields = ["tutorial_title",
            "tutorial_published",
            "tutorial_content",
            ]
    """
    #This display different sets of fields as provided
    fieldsets = [("Info", {"fields": ["tutorial_title", "tutorial_published"]} ),
                ("URL", {"fields": ["tutorial_slug"]}),
                ("Series", {"fields": ["tutorial_series"]}),
                ("Content", {"fields": ["tutorial_content"]} )
                ]

    formfield_overrides = {
        models.TextField: {"widget": TinyMCE()}
    }

class TutorialSeriesAdmin(admin.ModelAdmin):
    
    #This will display selected fields
    fields = ["tutorial_series",
            "series_summary",
            "tutorial_category",
            ]
    


admin.site.register(TutorialCategory)
admin.site.register(TutorialSeries, TutorialSeriesAdmin)
admin.site.register(Tutorial, TutorialAdmin)