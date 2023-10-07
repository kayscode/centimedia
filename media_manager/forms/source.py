from django import forms
from media_manager.utils import generate_organisation_select_form_choices


class CreateSourceMediaForm(forms.Form):
    url = forms.URLField(
        label="lien url",
        widget=forms.URLInput
    )

    source_type = forms.ChoiceField(
        label="type de source",
        widget=forms.Select,
        choices=[
            ("web-scrapping", "web-scrapping"),
            ("api", "api")
        ]
    )

    organisation = forms.ChoiceField(
        label="organisation",
        widget=forms.Select,
        choices=generate_organisation_select_form_choices()
    )


class DeleteSourceMediaForm(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput)


class UpdateSourceMediaForm(forms.Form):
    id = forms.IntegerField(label="source id", widget=forms.HiddenInput)
    url = forms.URLField(label="lien url", widget=forms.URLInput)
    is_approved = forms.BooleanField(label="approuve", widget=forms.CheckboxInput)

    organisation = forms.ChoiceField(
        label="organisation",
        widget=forms.Select,
        choices=generate_organisation_select_form_choices()
    )

    source_type = forms.ChoiceField(
        label="type de source",
        widget=forms.Select,
        choices=[
            ("web-scrapping", "web-scrapping"),
            ("api", "api")
        ]
    )
