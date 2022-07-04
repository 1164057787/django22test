from elasticsearch import Elasticsearch

# 实例化一个ip为localhost，端口为9200，
es = Elasticsearch('http://127.0.0.1:9200/')


# 查询所有的记录，默认返回10条
body={
    "query": {
        "match_all": {}
    }
}



# size的另一种指定方法
res=es.search(index='es_python', body=body, size=200)

print(res)
