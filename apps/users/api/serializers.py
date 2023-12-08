from rest_framework import serializers
from apps.users.models import User

class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','email','name','last_name')
            

class UserSerializer(serializers.ModelSerializer):
       
    class Meta:
        model = User
        fields = '__all__'
        model = User
    #Correcion de la encriptacion de la contraseña
    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()    
        return user
    #Correccion de la encriptacion de la contraseña
    def update(self, instance, validated_data):
        updated_user = super().update(instance, validated_data)
        updated_user.set_password(validated_data['password'])
        updated_user.save()
        return updated_user

       
class UserListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
    #Funcion para la visualizacion de los campos al listarlos   
    def to_representation(self, instance):
        return{
            'id': instance['id'],
            'username': instance['username'],
            'email': instance['email'],
            'password': instance['password']
        }       