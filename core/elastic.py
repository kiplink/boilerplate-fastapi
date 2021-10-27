from env import ELASTIC_HOST, ELASTIC_PORT
from elasticsearch import Elasticsearch

elastic_con = "%s:%s" % (ELASTIC_HOST, ELASTIC_PORT)
es = Elasticsearch([elastic_con])

# res = es.search(index="school", query={"match_all": {}})
# print("Got %d Hits:" % res['hits']['total']['value'])
# for hit in res['hits']['hits']:
#     print("%(zip)s %(name)s: %(street)s" % hit["_source"])
