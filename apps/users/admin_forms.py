from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField

# To be used for typing, to get the user model call 'get_user_model'.
CustomUser = get_user_model


class AddUserForm(forms.ModelForm):
    """Form to create new users, requiring password confirmation."""

    class Meta:
        model = get_user_model()
        fields = ("email", "first_name", "last_name")

    username = forms.CharField(label="username", required=False)

    # Add labels to differentiate the two password fields.
    password1 = forms.CharField(label="password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="confirm password", widget=forms.PasswordInput)

    def clean_password2(self) -> str:
        """Check that both passwords match.

        :return: password 2
        """

        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        # Check both password fields have data and if they match.
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")

        return password2

    def save(self, commit: bool = True) -> CustomUser:
        """Save the password in a hash format

        :param commit: commit the transaction to the database
        :return: CustomUser
        """

        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])

        if commit:
            user.save()

        return user


class UpdateUserForm(forms.ModelForm):
    """Form to update users. Changing of passwords is not allowed."""

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "password",
            "first_name",
            "last_name",
            "is_active",
            "is_staff",
        )

    def clean_password(self) -> str:
        return self.initial["password"]
