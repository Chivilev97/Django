from django.contrib import admin
from .models import MenuItems
from django import forms


class MyModelForm(forms.ModelForm):
    parent = forms.ModelChoiceField(
        queryset=MenuItems.objects.all(),
        empty_label='',
        required=False,
    )
    

    class Meta:
        model = MenuItems
        fields = ['parent','level', 'title', 'url', 'menu_name']


class MyModelAdmin(admin.ModelAdmin):
    form = MyModelForm
    list_display = ('title', 'id', 'parent', 'url', 'menu_name')
    


admin.site.register(MenuItems, MyModelAdmin)