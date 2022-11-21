from rest_framework import viewsets
from .serializers import MyBoardSerializer
from .models import MyBoard


class MyBoardView(viewsets.ModelViewSet):
    queryset = MyBoard.objects.all()
    serializer_class = MyBoardSerializer

    def perform_create(self, serializer):
        serializer.save()

