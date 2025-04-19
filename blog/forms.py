# forms.py
from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your email'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your message', 'rows': 5}),
        }

    def clean(self):
        """
        Custom validation to ensure all fields are filled out
        and the email is in a valid format.
        This method is called after the individual field validations.
        It raises a ValidationError if any field is invalid.
        It returns the cleaned data if all fields are valid.
        :return: cleaned_data
        """
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        subject = cleaned_data.get('subject')
        message = cleaned_data.get('message')

        if not name or not email or not subject or not message:
            raise forms.ValidationError("All fields are required.")

        return cleaned_data

    def save(self, commit=True):
        contact = super().save(commit=False)
        if commit:
            contact.save()
        return contact