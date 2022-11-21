from rest_framework import serializers
from .models import MyBoard


class MyBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyBoard
        fields = ('id', 'myname', 'mytitle', 'mycontent', 'mydate')
        