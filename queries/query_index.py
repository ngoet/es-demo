from es_connection import EsManagement

if __name__ == "__main__":

    es_connection = EsManagement()

    # Checking your cluster's health
    print(es_connection.es_client.cluster.health())

    # Check the number of documents in your index
    print(es_connection.es_client.count(index="netflix_movies_optimised"))  # TODO REMOVE optimised

    # Querying data
    # Query and filter contexts
    query = {
        "query": {
            "bool": {
                "must": [
                    {"match": {"type": "TV Show"}},
                ],
                "filter": [{"range": {"release_year": {"gte": 2021}}}],
            }
        }
    }

    results = es_connection.es_client.search(index="netflix_movies_optimised", body=query)

    # Result
    print([i["_source"]["title"] for i in results["hits"]["hits"]])

    # Inspecting the scores of the returned documents
    print([(i["_source"]["title"], i["_score"]) for i in results["hits"]["hits"]])

    # Querying data
    # Query and filter contexts
    updated_query = {
        "query": {
            "bool": {
                "filter": [{"range": {"release_year": {"gte": 2021}}}, {"term": {"type": "TV Show"}}],
            }
        }
    }

    results_updated_query = es_connection.es_client.search(index="netflix_movies_optimised", body=updated_query)

    # Result
    print([i["_source"]["title"] for i in results_updated_query["hits"]["hits"]])
