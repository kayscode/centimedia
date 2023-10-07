from django import forms
from organisations.utils import get_country_list


class CreateOrganisationForm(forms.Form):
    name = forms.CharField(label="nom du de l'organisation", widget=forms.TextInput)
    country = forms.ChoiceField(
        label="pays",
        widget=forms.Select,
        choices=get_country_list()
    )
    address = forms.CharField(label="address", widget=forms.Textarea)
    cover = forms.ImageField(label="cover", widget=forms.FileInput)


class DeleteOrganisationForm(forms.Form):
    id = forms.IntegerField(widget=forms.HiddenInput)


class UpdateOrganisationForm(CreateOrganisationForm, DeleteOrganisationForm):
    pass
