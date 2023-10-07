from django import forms
from media_manager.utils import generate_organisation_select_form_choices


class CreateMediaFileForm(forms.Form):
    title = forms.CharField(label="titre")
    file_cover = forms.ImageField(label="image", widget=forms.FileInput)
    file = forms.FileField(
        label="uploader fichier",
        widget=forms.FileInput,
    )

    organisation = forms.ChoiceField(
        label="organisation",
        widget=forms.Select,
        choices=generate_organisation_select_form_choices()
    )

    media_type = forms.ChoiceField(
        label="type de fichier",
        widget=forms.Select,
        choices= [
            ("audio","audio"),
            ("video","video")
        ]
    )


class DeleteMediaFileForm(forms.Form):
    id = forms.IntegerField(label="id", widget=forms.HiddenInput)


class UpdateMediaFileForm(forms.Form):
    id = forms.IntegerField(label="id", widget=forms.HiddenInput)
    title = forms.CharField(label="titre", widget=forms.TextInput)
    file_cover = forms.ImageField(label="image", widget=forms.FileInput)
    file = forms.FileField(label="uploader fichier",widget=forms.FileInput)
    organisation = forms.ChoiceField(
        label="organisation",
        widget=forms.Select,
        choices= generate_organisation_select_form_choices()
    )
    media_type = forms.ChoiceField(
        label="type de fichier",
        widget=forms.Select,
        choices=[
            ("audio", "audio"),
            ("video", "video")
        ]
    )
