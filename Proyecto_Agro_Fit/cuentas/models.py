from django.db import models
from django.contrib.auth.models import User #Esta importacion es para poder usar el modelo de usuario que ya viene con django y asi poder hacer la relacion con el modelo de perfil OSEA CON CADA TABLA

# Create your models here.

#Estas son tuplas con las opciones del los menus desplegables.    
DEPENDENCIAS = (
    ('instructor gym', 'Instructor GYM'),
    ('coordinador', 'Coordinador'),
)
    
CENTROS_FORMACION = (
    ('centro agropecuario', 'Centro Agropecuario'),
    ('centro industrial', 'CTPI'),
)


#---AQUI SE DEFINE LA TABLA Y LOS CAMPOS DE LA TABLA, CADA CAMPO ES UNA COLUMNA EN LA TABLA DE LA BASE DE DATOS.
    #Estos otros campos que permiten estar nulos al momento del registro 
      # blank=True (permite enviarlo vacío desde el formulario)
      # null=True (permite guardar un valor nulo en la base de datos

#TABLA PARA FUNCIONARIOS
class PerfilFuncionario(models.Model):
    
    #aqui se hace la relacion con el modelo de usuario Osea decimos que cada perfil va a tener un usuario y que si se elimina el usuario se elimine el perfil tambien.
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil_funcionario') #related_name es para poder acceder a los datos del perfil desde el modelo de user, es decir, si tengo un usuario puedo acceder a su perfil con user.perfil_funcionario
    
    dependencia = models.CharField(max_length=50, choices=DEPENDENCIAS)
    centro_formacion = models.CharField(max_length=50, choices=CENTROS_FORMACION)
    dependencia = models.CharField(max_length=50, choices=DEPENDENCIAS)
    
    def __str__(self):
        return f'Funcionario: {self.user}-{self.dependencia}'
     

#TABLA PARA APRENDIZES
class PerfilAprendiz(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil_aprendiz')
    numero_ficha = models.CharField(max_length=12, null=False, blank=False)
    
    def __str__(self):
        return f'funcionario: {self.user} - {self.numero_ficha}'