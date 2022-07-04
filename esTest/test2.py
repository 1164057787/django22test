

from elasticsearch import Elasticsearch

# 实例化一个ip为localhost，端口为9200，
es = Elasticsearch('http://127.0.0.1:9200/')
"""索引名 es_python,ignore=400，表示忽视400这个错误，如果存在es_python时，会返回400"""
es.indices.delete(index='es_python')
es.indices.create(index='es_python',ignore=400)


body = {'name':'刘婵',"age":6,
		"sex":"male",'birthday':'1984-01-01',
		"salary":-12000}
res=es.index(index='es_python',doc_type='_doc',body=body)
print(res)


doc = [
    {'index':{'_index':'es_python','_type':'_doc','_id':1}},
    {'name':'赵云','age':25,'sex':'male','birthday':'1995-01-01','salary':8000},
    {'index':{'_index':'es_python','_type':'_doc','_id':2}},
    {'name':'张飞','age':24,'sex':'male','birthday':'1996-01-01','salary':8000},
    {'create':{'_index':'es_python','_type':'_doc','_id':3}},
    {'name':'关羽','age':23,'sex':'male','birthday':'1996-01-01','salary':8000},
]
res2=es.bulk(index='es_python',doc_type='_doc',body=doc)

print(res2)

body = {
    'from': 0,  # 从0开始
    'size': 2  # 取2个数据。类似mysql中的limit 0, 20。 注：size可以在es.search中指定，也可以在此指定，默认是10
}

# 定义过滤字段，最终只显示此此段信息
# filter_path=['hits.hits._source.ziduan1',  # 字段1
#              'hits.hits._source.ziduan2']  # 字段2

# res3=es.search(index='es_python', filter_path=filter_path, body=body)
res3=es.search(index='es_python', body=body)



print(res3)
