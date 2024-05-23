from rest_framework import serializers
from autenticacion.models import User

class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input:type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'password2')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user = User(email=self.validated_data['email'], username=self.validated_data['username'])
        password = self.validated_data['password']
        password2 = self.validated_data['password2']  # Corregido de 'password' a 'password2'
        if password != password2:
            raise serializers.ValidationError({'password': 'Las contraseñas no coinciden'})
        user.set_password(password)
        user.save()
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
