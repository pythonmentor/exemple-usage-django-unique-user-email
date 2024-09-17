from unique_user_email import forms as auth_forms


class AuthenticationForm(auth_forms.AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["login"].label = "Nom d'utilisateur ou adresse email"
        self.fields["password"].label = "Mot de passe"
