from django.contrib import admin
from .models import Player, Goal, Match
from django import forms


admin.site.register(Player)
admin.site.register(Goal)
admin.site.register(Match)


# class MatchAdminForm(forms.ModelForm):
#     class Meta:
#         model = Match
#         fields = '__all__'  # Or specify the fields you want to include

#     def clean_pre_report(self):
#         print(self.cleaned_data)
#         return self.cleaned_data["pre_report"]


# class MatchAdmin(admin.ModelAdmin):
#     form = MatchAdminForm


# admin.site.register(Match, MatchAdmin)
