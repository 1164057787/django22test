from elasticsearch import Elasticsearch


from elasticsearch import Elasticsearch

# 实例化一个ip为localhost，端口为9200，
es = Elasticsearch('http://127.0.0.1:9200/')

es.indices.delete(index='py_index01',ignore=404)
es.indices.create(index='py_index01',ignore=400)


body1={
    'name':'tony',
    'age':56,
    'city':'shanghai',
    'hobby':'singing,dncing,reding'
}


body2={
    'name':'john',
    'age':24,
    'city':'shenzhen',
    'hobby':'running,reading'
}

body3={
    'name':'zhangsan',
    'age':36,
    'city':'shenzhen',
    'hobby':'hilking,eting'
}

es.index(index='py_index01',id=1,body=body1)
es.index(index='py_index01',id=2,body=body2)
es.index(index='py_index01',id=3,body=body3)

query={
    'query':{
        "match_all":{}
    }
}
query2={
    'query':{
        'term':{
            'name':'zhangsan'
        }
    }
}

result=es.search(index="example",body=query2)

print(result)


