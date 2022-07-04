class MyResponse():
    def __init__(self):
        self.status=100
        self.msg="成功"
    # def __init__(self):
    #     print("我是初始化方法")
    #     self.status=100
    #     self.msg="成功"
    @property
    def get_dict(self):
        return self.__dict__

if __name__=='__main__':
    res=MyResponse()
    res.status=101
    res.msg="failed"

    res.data="ggh"
    print(res.get_dict)

