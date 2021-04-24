from elasticsearch import Elasticsearch
import json
import os


es_client = Elasticsearch([os.environ["HOST"]], http_auth=(os.environ["ACCESS_KEY"], os.environ["ACCESS_SECRET"]))
index = "netflix_mapping_optimized"

# Regex
regex_query = {"query": {"regexp": {"title": "war.*"}}}

regex_query_results = es_client.search(index=index, body=regex_query)
print(json.dumps(regex_query_results["hits"], indent=2))

# Script query
script_query = {
    "query": {
        "bool": {
            "filter": {
                "script": {
                    "script": {
                        "source": "doc['release_year'].value > params.start_year",
                        "lang": "painless",
                        "params": {"start_year": 2018},
                    }
                }
            }
        }
    }
}

script_query_results = es_client.search(index=index, body=script_query)
print(json.dumps(script_query_results["hits"], indent=2))


# Terms aggregation
terms_agg_query = {
    "size": 0,
    "sort": "release_year",
    "aggs": {"release_years": {"terms": {"field": "release_year", "size": 5, "order": {"_term": "asc"}}}},
}


terms_agg_query_results = es_client.search(index=index, body=terms_agg_query)
print(json.dumps(terms_agg_query_results["aggregations"], indent=2))


# Stats
stats_query = {"size": 0, "aggs": {"release_year_stats": {"stats": {"field": "release_year"}}}}

stats_query_results = es_client.search(index=index, body=stats_query)
print(json.dumps(stats_query_results["aggregations"], indent=2))
