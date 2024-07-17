from django import forms
#from django.forms import fields
#from .models import Cliente 


#class formularioCadastro(forms.ModelForm):
    #class Meta:
        #model = Cliente

        #fields = [
              #'first_name',
              #'last_name',
              #'username',
              #'password',
              #'cpf',
              #'cidade',
              #'telefone',
                  
                  
        #]

class Cliente(forms.Form):
    nome = forms.CharField(max_length=30)
    email=forms.CharField(max_length=100)
    senha=forms.CharField(max_length=100)
    confimesenha=forms.CharField(max_length=100)
