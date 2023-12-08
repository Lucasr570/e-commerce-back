from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from apps.users.authentication_mixins import Authentication
from apps.products.api.serializers.product_serializer import ProductSerializer

# Clase gral para enlazar las url del crud en un routers..
class ProductViewSet(Authentication,viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    
    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id= pk,state = True).first()# noqa: E501
    
    def list(self,request):
        '''
        Retorna un listado de todos los productos
        
        params ---> nombre del producto
        '''
        product_serializer = self.get_serializer(self.get_queryset(),many=True)
        return Response (product_serializer.data, status=status.HTTP_200_OK)
    
    def create(self,request):
        '''
        Acceso a la creación de productos
        
        params ---> nombre del producto
        '''
        serializer = self.serializer_class(data = request.data) 
        if serializer.is_valid(): 
            serializer.save()
            return Response({'message': 'Producto creado correctamente!'}, status = status.HTTP_201_CREATED)  # noqa: E501
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk= None):
        '''
        Acceso a actualizar productos
        
        params ---> nombre, descripción
        '''
        if self.get_queryset(pk):
            product_serializer = self.serializer_class(self.get_queryset(pk), data = request.data)# noqa: E501
            if product_serializer.is_valid():
                product_serializer.save()
                return Response({'message': 'Producto actualizado correctamente!'})# noqa: E501 
            return Response(product_serializer.errors,status=status.HTTP_400_BAD_REQUEST) # noqa: E501    
    
    def destroy(self, request,pk=None):
        '''
        Acceso a eliminar productos
        
        params ---> id
        '''
        product = self.get_queryset().filter(id = pk).first()
        if product:
            product.state= False
            product.save()
            return Response ({'message':'Producto eliminado correctamente!'},status= status.HTTP_200_OK)  # noqa: E501
        return Response({'error':'No existe un producto con estos datos!'},status=status.HTTP_400_BAD_REQUEST)  # noqa: E501


                