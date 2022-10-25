from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import MyBoard

class MyBoardListView(ListView):
    # 전달되는 queryset의 이름 : object_list
    # render 되는 template의 이름 : myboard_list.html

    def get_queryset(self):
        return MyBoard.objects.all().order_by("-mydate")

class MyBoardDetailView(DetailView):
    model = MyBoard
    template_name = 'cbstest/detail.html'
    context_object_name = "dto"
    pk_url_kwarg = "id" # path 함수로부터 전달받을 pk의 키워드 이름