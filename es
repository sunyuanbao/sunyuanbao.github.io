from elasticsearch import Elasticsearch
es = Elasticsearch(hosts="http://172.16.2.103:9200/")
print(es.info())

#result=es.indices.create(index='news',ignore=400)  //创建一个新的索引并打印
#print(es.result())
