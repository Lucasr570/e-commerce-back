from django.db import models
from simple_history.models import HistoricalRecords
from apps.base.models import BaseModel

# Create your models here.
class MeasureUnit(BaseModel):
    
    description = models.CharField('Descriptión',max_length= 50,blank= False,null= False,unique= True)  # noqa: E501
    historical = HistoricalRecords()  
    
    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by =value 
        
    class Meta:
        verbose_name = 'Unidad de Medida'
        verbose_name_plural = 'Unidades de Medidas' 
        
    def __str__(self):
        return self.description
#Categoria del Producto
class CategoryProduct(BaseModel):
    
    description = models.CharField('Descriptión',max_length= 50,unique=True, null= False, blank= False)  # noqa: E501
    historical = HistoricalRecords()
    
    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by =value     
    
    class Meta:
        verbose_name = 'Categoría de producto'
        verbose_name_plural = 'Categorías de Productos' 
    
    def __str__(self):
        return self.description
    
#Indicador de Descuento
class Indicator(BaseModel):
    
    descount_value = models.PositiveSmallIntegerField(default= 0) 
    category_product = models.ForeignKey(CategoryProduct ,on_delete=models.CASCADE,verbose_name= 'Indicador de Oferta')  # noqa: E501
    historical = HistoricalRecords()
    
    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by =value     
    
    class Meta:
        verbose_name = 'Indicador de Oferta'
        verbose_name_plural = 'Indicadores de Ofertas' 
    
    def __str__(self):
        return f'Oferta de la categoría{self.category_product}: {self.descount_value}%' 
    
    
 #Modelo Producto (Principal)
class Product(BaseModel):
    
    name = models.CharField('Nombre de Producto',max_length= 150,blank= False,null= False,unique= True)  # noqa: E501
    description = models.TextField('Descripción de Producto',blank= False,null= False)
    image =models.ImageField('Imagen del Producto',upload_to='product/',blank=True,null=True)  # noqa: E501
    measure_unit = models.ForeignKey(MeasureUnit ,on_delete=models.CASCADE, null= True, verbose_name= 'Unidad de Medida')  # noqa: E501
    category_product =models.ForeignKey(CategoryProduct, on_delete= models.CASCADE, null= True, verbose_name= 'Categoría de Producto')  # noqa: E501
    historical = HistoricalRecords() 
    
    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by =value     
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos' 
    
    def __str__(self):
        return self.name