from django.urls import path

#from pizzaria.views import *
from . import views



urlpatterns = [
    
    path('home', views.home),
    path('cardapio', views.cardapio),
    path('indexcadastrado', views.indexcadastrado, name='indexcadastrado'),
    path('menu', views.menu),
    path('pagamento', views.pagamento),
    path('login',views.login, name = 'login '),
    path('compra', views.compra),
    path('cadastro', views.cadastro, name= 'cadastro'),
    path('contato', views.contato, name= 'contato'),
    

   
]   