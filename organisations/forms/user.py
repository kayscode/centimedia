from django import forms
from organisations.utils import generate_organisation_select_form_choices


class CreateUserForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput)
    avatar = forms.ImageField(widget=forms.FileInput)
    email = forms.EmailField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)
    organisation = forms.ChoiceField(choices=generate_organisation_select_form_choices(), widget=forms.Select)
    is_active = forms.BooleanField(widget=forms.CheckboxInput)
    account_type = forms.ChoiceField(
        choices=[
            ("admin", "admin"),
            ("super admin", "super admin")
        ]
    )


class DeleteUserForm(forms.Form):
    id = forms.IntegerField(widget=forms.HiddenInput)


class UpdateUserForm(CreateUserForm, DeleteUserForm):
    pass
