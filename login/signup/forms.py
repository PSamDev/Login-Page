from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User 

class SignUp(UserCreationForm):
    first_name = forms.CharField(label="First Name", max_length=500, required=True)
    last_name = forms.CharField(label="Last Name", max_length=500, required=True)
    email = forms.EmailField(label="Email", required=True)
   
    
    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password1", "password2")
        
    def save(self, commit = True):
        user = super(SignUp,self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        
        if commit:
            user.save()
            return user 