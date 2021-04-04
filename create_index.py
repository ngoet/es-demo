import json

from es_connection import EsManagement
from mappings import netflix_mapping


if __name__ == "__main__":
    es_connection = EsManagement()
    es_connection.create_index(index_name="netflix_movies", mapping=netflix_mapping)
    print(json.dumps(es_connection.es_client.indices.get_mapping(index="netflix_movies"), indent=1))
