from django import forms

from apps.account.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(max_length=256)

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
            "phone",
            "password",
            "staff",
            "admin"
        ]

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
