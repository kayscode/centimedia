from django import forms


class ApproveNotificationForm(forms.Form):
    id = forms.IntegerField(widget=forms.HiddenInput)
    media_id = forms.IntegerField(widget=forms.HiddenInput)


class RejectNotificationForm(forms.Form):
    id = forms.IntegerField(label="id", widget=forms.HiddenInput)
    media_id = forms.IntegerField(widget=forms.HiddenInput)
