from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from appsers.models import Student
from appsers.ser import StudentSer
from rest_framework.response import Response
from django.http import JsonResponse
from appsers.ser import StuModelSerializer

from appsers.utils import MyResponse


class StuView(APIView):
    # 查询一个
    def get(self, request, pk):
        stu = Student.objects.filter(sid=pk).first()  # 拿到queryset,这里的sid是model的字段

        # 实例化 调用init实例化
        stu_ser = StudentSer(stu)
        # stu_ser.data就是序列化后的字典
        # print(stu_ser.data)
        return Response(stu_ser.data)  # DRF自己封装了response
        # 如果不用模板 就用jsonresponse
        # return JsonResponse(stu_ser.data)

    # 修改一个
    def put(self, request, pk):
        response_msg = {'status': 100, "msg": "success"}
        stu = Student.objects.filter(sid=pk).first()  # 找到该对象
        stu_ser = StudentSer(stu, request.data)  # 序列化
        if stu_ser.is_valid():
            stu_ser.save()
            response_msg['data'] = stu_ser.data
        else:
            response_msg['status'] = 101
            response_msg['msg'] = '数据校验失败'
            response_msg['data'] = stu_ser.errors

        return Response(response_msg)

    # 删除
    def delete(self, request, pk):
        ret = Student.objects.filter(sid=pk).delete()
        return Response({'status': 100, "msg": "delete success"})


class StusView(APIView):
    # 查询所有
    # def get(self,request):
    #     stus=Student.objects.all()
    #     stus_ser=StudentSer(stus,many=True)  #序列化多条many等于true 一条的话不用
    #     response_msg = {'status': 100, "msg": "success"}
    #     response_msg['data']=stus_ser.data
    #
    #     return Response(response_msg)

    # 用myresponse
    def get(self, request):
        response = MyResponse()
        stus = Student.objects.all()
        stus_ser = StudentSer(stus, many=True)  # 序列化多条many等于true 一条的话不用
        # response_msg = {'status': 100, "msg": "success"}
        response.data = stus_ser.data

        return Response(response.get_dict)

    # 新增一条
    def post(self, request):
        response_msg = {'status': 100, "msg": "success"}
        # 修改才有instance 新增没有instance 只有data 此处位置要对
        stu_ser = StudentSer(data=request.data)
        # stu_ser=StudentSer(request.data)   会报错

        if stu_ser.is_valid():
            stu_ser.save()
            response_msg['data'] = stu_ser.data
        else:
            response_msg['status'] = 103
            response_msg["msg"] = "数据校验失败"
            response_msg['data'] = stu_ser.errors

        return Response(response_msg)


# 测试模型序列化器
class StusView2(APIView):
    def get(self, request):
        response = MyResponse()
        stus = Student.objects.all()
        stus_ser = StuModelSerializer(stus, many=True)  # 序列化多条many等于true 一条的话不用
        # response_msg = {'status': 100, "msg": "success"}
        response.data = stus_ser.data

        return Response(response.get_dict)


