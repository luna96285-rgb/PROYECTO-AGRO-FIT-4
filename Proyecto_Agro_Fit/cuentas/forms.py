from django import forms
from django.contrib.auth.forms import UserCreationForm # Trae una herramieta de Django Para crear nuevos usuarios
#  - crea automaticamente las casillas o campos de nombre de usuario, contra y confirmacion de contra y trae el cifrado y las verificacion de contra(osea mas de 7 carecteres y lo demas)

from django.contrib.auth.models import User # aqui se importa el modelo de usuario que ya viene con django para poder hacer la relacion con el modelo de tabla creada

from .models import DEPENDENCIAS, CENTROS_FORMACION


#OPCIONES DE LOS MENUS DESPLEGABLES
dependencias_opciones = [('','Seleciona una Dependencia')] + list(DEPENDENCIAS)
centro_formacion = [('','Seleciona una Dependencia')] + list(CENTROS_FORMACION)


#FORMULARIO PARA FUNCIONARIOS
class FormularioRegistroFuncionario(UserCreationForm):
    
    #Campos del formulario
    first_name = forms.CharField(max_length=20, required=True, label="Nombre")
    last_name = forms.CharField(max_length=20, required=True, label="Apellido")
    email = forms.EmailField(required=True, label="Correo")
    
    dependencia = forms.ChoiceField(choices=dependencias_opciones, required=True)
    centro_formacion = forms.ChoiceField(choices=centro_formacion, required=True)
    
    #Aqui decimos los campos que usamos de auth_user 
    class Meta(UserCreationForm.Meta):
        
        model = User #pasamos el modelo osea que es decir de la tabla (auth_user) 
        fields = ['first_name','last_name','email'] #Estos son los campos que modificamos y se los devovolvemos
        


#FORMULARIO PARA APRENDIZES
class FormularioRegistroAprendiz(UserCreationForm):
    
    #campos de formulario
    first_name = forms.CharField(max_length=20, required=True, label="Nombre")
    last_name = forms.CharField(max_length=20, required=True, label="Apellido")
    email = forms.EmailField(required=True, label="Correo")
        
    numero_ficha = forms.CharField(max_length=12, required=True)
    
    class Meta(UserCreationForm.Meta):
        user = User
        fields = ['first_name','last_name','email']