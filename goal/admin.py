from django.contrib import admin
from .models import Player, Goal, Match
from django import forms


admin.site.register(Player)
admin.site.register(Goal)
# admin.site.register(Match)


class YourModelAdminForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = '__all__'  # Or specify the fields you want to include

    def clean_pre_report(self):
        return self.cleaned_data.get('pre_report', '')


class YourModelAdmin(admin.ModelAdmin):
    form = YourModelAdminForm


admin.site.register(Match, YourModelAdmin)
