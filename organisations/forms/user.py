from django import forms
from organisations.utils import generate_organisation_select_form_choices


class CreateUserForm(forms.Form):
    avatar = forms.ImageField(
        widget=forms.FileInput(
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


class AdminCreateUserForm(CreateUserForm):
    username = forms.CharField(
        widget=forms.TextInput(
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
    pass


class AdminUpdateUserForm(DeleteUserForm, AdminCreateUserForm):
    pass
