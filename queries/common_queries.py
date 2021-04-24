from elasticsearch import Elasticsearch
import json
import os


es_client = Elasticsearch([os.environ["HOST"]], http_auth=(os.environ["ACCESS_KEY"], os.environ["ACCESS_SECRET"]))
index = "netflix_mapping_optimized"

# Match
title = "House of Cards"
match_query = {
    "query": {
        "match": {
            "title": {"query": title, "operator": "and"},
        }
    }
}

match_results = es_client.search(index=index, body=match_query)
print(json.dumps(match_results["hits"], indent=2))

assert len(match_results["hits"]["hits"]) == 1
assert [i["_source"]["title"] for i in match_results["hits"]["hits"]][0] == title

# Term
type = "TV Show"
term_query = {
    "size": 5,
    "query": {
        "term": {
            "type": {"value": type},
        }
    },
}

term_results = es_client.search(index=index, body=term_query)
print(json.dumps(term_results["hits"], indent=2))

assert all([i["_source"]["type"] == type for i in term_results["hits"]["hits"]])

# Range
year = 2012
range_query = {"size": 100, "query": {"range": {"release_year": {"lte": year}}}}

range_results = es_client.search(index=index, body=range_query)
print(json.dumps(range_results["hits"], indent=2))

assert max([i["_source"]["release_year"] for i in range_results["hits"]["hits"]]) == year
