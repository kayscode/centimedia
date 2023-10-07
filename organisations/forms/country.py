from django import forms


class CreateCountryForm(forms.Form):
    continent = forms.ChoiceField(
        label="continent",
        widget=forms.Select,
        choices=[
            ("Af", "Afrique"),
            ("Eu", "Europe"),
            ("Asie", "Asie"),
            ("Amerique", "Amerique"),
            ("Oceanie", "Oceanie"),
        ],
    )
    name = forms.CharField(label="nom du pays", widget=forms.TextInput)


class DeleteCountryForm(forms.Form):
    id = forms.IntegerField(widget=forms.HiddenInput)


class UpdateCountryForm(CreateCountryForm, DeleteCountryForm):
    pass
