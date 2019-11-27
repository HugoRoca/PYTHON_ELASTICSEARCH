from elasticsearch import Elasticsearch
import requests
import json

es = Elasticsearch([{"host": "localhost", "port": 9200}])

i = 18
r = requests.get('http://localhost:9200') 

while r.status_code == 200:
    r = requests.get("http://swapi.co/api/people/" + str(i))
    es.index(index="star_wars", doc_type="people",
             id=i, body=json.loads(r.content))
    i = i+1
