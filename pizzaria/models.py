from django.db import models
#from django import fields
from django import forms
# Create your models here
    
class Fornecedor(models.Model):
     idfornecedor = models.IntegerField(primary_key=True)
     nome= models.CharField(max_length=50, null=False)
     cnpj=models.CharField(max_length=14, null=False)
     produto = models.CharField(max_length=50, null=False)

     def __str__(self):
      return self.nome 
   


class Produtos(models.Model):
    idproduto= models.IntegerField(primary_key=True)
    validade=models.DateTimeField(null=False)  



class Pedido(models.Model):
    idpedido = models.IntegerField(primary_key=True)
    pagamento = models.IntegerField()



class Cliente(models.Model):
    idcliente = models.IntegerField(primary_key=True)
    nome = models.CharField( max_length=50)
    cpf = models.CharField( max_length=50, null= False)
    telefone =  models.CharField( max_length=11, null= False)
    nome = models.CharField( max_length=50, null= False)
    endereco = models.CharField( max_length=200, null=False)
    Pedido = models.ForeignKey(Pedido, on_delete=models.SET_NULL, null=True)

    def __str__(self):
     return self.nome 
   

class Funcionarios(models.Model):
    idfuncionarios = models.IntegerField(primary_key=True)
    nome = models.CharField( max_length=50)  
    datanasc= models.DateField(
                help_text=" formato <em>YYYY-MM-DD</em>")
    funcao= models.CharField( max_length=50, null= False )

    def __str__(self):
     return self.nome 
   


 
         
     
  
   
