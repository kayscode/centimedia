from django import forms
from organisations.utils import get_country_list


class CreateOrganisationForm(forms.Form):
    name = forms.CharField(
        label="nom de la branche",
        widget=forms.TextInput(
            attrs={}
    ))

    email = forms.EmailField(
        label="email",
        widget=forms.EmailInput(
            attrs={}
        ))

    country = forms.ChoiceField(
        label="pays",
        widget=forms.Select(
            attrs={

            }
        ),
        choices=get_country_list()
    )

    address = forms.CharField(
        label="address",
        widget=forms.Textarea(
            attrs={}
        ))

    cover = forms.ImageField(
        label="cover",
        widget=forms.FileInput(
            attrs={}
        ))


class DeleteOrganisationForm(forms.Form):
    id = forms.IntegerField(widget=forms.HiddenInput)


class UpdateOrganisationForm(CreateOrganisationForm, DeleteOrganisationForm):
    pass
