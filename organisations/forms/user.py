from django import forms
from organisations.utils import generate_organisation_select_form_choices


class CreateUserForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={

            }
        )
    )
    avatar = forms.ImageField(
        widget=forms.FileInput(
            attrs={

            }
        )
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={

            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={

            }
        )
    )

    organisation_id = forms.ChoiceField(
        choices=generate_organisation_select_form_choices(),
        widget=forms.Select(
            attrs={

            }
        )
    )

    account_type = forms.ChoiceField(
        choices=[
            ("admin", "admin"),
            ("super admin", "super admin")
        ],
        widget=forms.Select(
            attrs={

            }
        )
    )

    is_active = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={

            }
        )
    )


class DeleteUserForm(forms.Form):
    id = forms.IntegerField(widget=forms.HiddenInput)


class UpdateUserForm(CreateUserForm, DeleteUserForm):
    is_active = forms.BooleanField(widget=forms.HiddenInput)


class AdminUpdateUserForm(CreateUserForm, DeleteUserForm):
    pass
