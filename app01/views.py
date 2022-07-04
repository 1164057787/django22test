import json

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse

from django.views import View


def login(request):
    return HttpResponse('<h1>这是视图函数login def</h1>')
    # return JsonResponse({"code":200,"message":"success"})

class LoginClass(View):

    def get(self,request):
        return HttpResponse('get method')

    def post(self,request):
        # print(len(request.body))
        request_data=request.body

        try:
            request_data=json.loads(request_data)
        except:
            result_data={'code':"1","msg":"请求出错"}

        print(request_data)

        result={"code":'0',"message":"success","data":str(request_data)}
        # return HttpResponse('post method')
        return JsonResponse(result)

    def delete(self,request):
        return HttpResponse('delete method')



from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from  .models import Book
from .sers import BookModelSerializer
class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer