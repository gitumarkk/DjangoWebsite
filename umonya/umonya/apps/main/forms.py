from django import forms
from captcha.fields import ReCaptchaField


class ContactForm(forms.Form):
    required = "required"
    name = forms.CharField(label="Name", required=True,
                           widget=forms.TextInput(attrs={"class": required, required: ""}))

    email = forms.EmailField(label="Email Address", required=True,
                             widget=forms.TextInput(attrs={"class": required, required: "",
                                                    "type": "email"}))

    text = forms.CharField(label="Talk to us",
                           widget=forms.Textarea(attrs={}))

    captcha = ReCaptchaField(
              public_key="6Le5IuQSAAAAAGeTlu2uuj2AcOG-1eDB-qdtz8Xf",
              private_key="6Le5IuQSAAAAABqGjiSAhyEVgBM-X0xkJGpKrJCG"
              )
