from django.shortcuts import render

# Create your views here.

from django.core.cache import cache

import time
from django.views.decorators.cache import cache_page
from django.http import HttpResponse


#全局缓存
@cache_page(15)
def test_cache(request):
    t = time.time()
    return HttpResponse('t is %s'%(t))


#局部缓存
def test_cache2(request):

    value = "Hello World, Hello Django Cache"
    cache.set('key', value)
    cache_result = cache.get('key')
    print('5 seconds ago, result: ', cache_result)

    # 设置5秒超时
    value2 = 'Hello World, Hello Django Timeout Cache.'
    cache.set('key2', value2, 5)
    cache_result2 = cache.get('key2')
    print('5 seconds ago, result2: ', cache_result2)
    time.sleep(5)
    cache_result2 = cache.get('key2')
    print('5 seconds later, result: ', cache_result)
    print('5 seconds later, result2: ', cache_result2)


    return HttpResponse('缓存测试')

