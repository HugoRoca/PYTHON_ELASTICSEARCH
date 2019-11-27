from elasticsearch import Elasticsearch
import json

es = Elasticsearch([{"host": "localhost", "port": 9200}])

query = {
    "query":{
        "match":{
            "name":"Darth Vader"
        }
    }
}

r = es.search(index="star_wars", body=query)

print(json.dumps(r, separators=(",",":")))
print(r)
