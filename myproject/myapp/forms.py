from django import forms

from .models import Contact  # Add this import statement

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    
    # method to handle the form after validation
    def send_email(self):
        # Add your email sending logic here
        print(f"Sending email from{self.cleaned_data['email']} with message: {self.cleaned_data['message']}")
        
       
       
       
        
    # Method to save the form data to the database
    def save(self):
        # Save the form data to the Contact model
        contact = Contact(
            name=self.cleaned_data['name'],
            email=self.cleaned_data['email'],
            message=self.cleaned_data['message']
        )
        contact.save()  # Save the data to the database
        return contact