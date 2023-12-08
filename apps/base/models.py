from django.db import models

class BaseModel(models.Model):
    
    id = models.AutoField(primary_key = True)
    state = models.BooleanField('Estado',default = True)
    created_date = models.DateField('Fecha de Creación', auto_now= False, auto_now_add= True)  # noqa: E501
    modified_date = models.DateField('Fecha de Modificación', auto_now= True, auto_now_add= False) # noqa: E501
    delete_date = models.DateField('Fecha de Eliminación', auto_now= True, auto_now_add= False)  # noqa: E501
    
    class Meta:
        
        abstract = True
        verbose_name = 'Modelo Base'
        verbose_name_plural = 'Modelos Base'
        