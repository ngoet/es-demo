import json
import os

from es_connection import EsManagement


if __name__ == "__main__":
    es_connection = EsManagement()
    es_connection.create_index(index_name="netflix_movies_dynamic_field_mapping")
    es_connection.populate_index(
        index_name="netflix_movies_dynamic_field_mapping", path=os.path.join("../data", "netflix_titles.csv")
    )
    print(
        json.dumps(es_connection.es_client.indices.get_mapping(index="netflix_movies_dynamic_field_mapping"), indent=1)
    )
