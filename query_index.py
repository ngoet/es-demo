from es_connection import EsManagement

if __name__ == "__main__":

    es_connection = EsManagement()

    # Checking your cluster's health
    print(es_connection.es_client.cluster.health())

    # Check the number of documents in your index
    print(es_connection.es_client.count(index="netflix_movies"))

    # Querying data
    # Query and filter contexts
    query = {
        "query": {
            "bool": {
                "must": [
                    {"match": {"type": "TV Movie"}},
                ],
                "filter": [
                    {"range": {"release_year": {"gte": 2015}}}
                ]
            }
        }
    }

    results = es_connection.es_client.search(index="netflix_movies", body=query)

    # Inspecting the scores of the returned documents
    print([(i["_source"]["title"], i["_score"]) for i in results["hits"]["hits"]])
