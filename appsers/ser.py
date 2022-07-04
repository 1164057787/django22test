from rest_framework.serializers import Serializer, ModelSerializer
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from appsers.models import Student


class StudentSer(Serializer):
    sid = serializers.CharField()
    sname = serializers.CharField()
    sprice = serializers.CharField()
    # sprice=serializers.DecimalField()  这样也可以 但影响不大
    sage = serializers.CharField()
    shome = serializers.CharField(max_length=4)

    def validate_sprice(self, data):  # 局部校验
        if float(data) > 30:
            return data
        else:
            raise ValidationError("价格数据校验失败")

    def validate(self, validated_data):  # 全局校验函数
        # print(validated_data)
        sname = validated_data.get('sname')
        shome = validated_data.get('shome')
        if sname == shome:
            raise ValidationError("s??")
        else:
            return validated_data

    def update(self, instance, validated_data):
        # instance是stu对象，validated_data是校验后的数据
        instance.sid = validated_data.get("sid")
        instance.sname = validated_data.get("sname")
        instance.sprice = validated_data.get("sprice")
        instance.sage = validated_data.get("sage")
        instance.shome = validated_data.get("shome")
        instance.save()  # 等于stu.save django 提供的

        return instance

    def create(self, validated_data):
        instance = Student.objects.create(**validated_data)
        # Student.objects.create(sid=validated_data.get("sid"))#传统写法 一个一个的取
        return instance


# 模型序列化器
class StuModelSerializer(ModelSerializer):
    class Meta:
        model = Student  # 对应到model.py中的模型
        # fields="__all__"
        fields = ('sid', 'sname')  # 指定序列化字段
        # exclude=('**')  #排除外的
