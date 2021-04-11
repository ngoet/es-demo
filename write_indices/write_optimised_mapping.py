import json
import os

from es_connection import EsManagement
from mappings import netflix_mapping_optimized


if __name__ == "__main__":
    es_connection = EsManagement()
    es_connection.create_index(index_name="netflix_movies_optimised", mapping=netflix_mapping_optimized)
    es_connection.populate_index(
        index_name="netflix_movies_optimised", path=os.path.join("../data", "netflix_titles.csv")
    )
    print(json.dumps(es_connection.es_client.indices.get_mapping(index="netflix_movies_optimised"), indent=1))
