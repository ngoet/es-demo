import json
import os
from dataclasses import dataclass
from typing import Dict


from es_connection import EsManagement
from mappings import (
    netflix_mapping_optimized,
    netflix_movies_unindexed_fields,
    netflix_movies_remove_normalisation_factors,
)


@dataclass
class MappingEntry:
    mapping: Dict
    name: str

    @property
    def __name__(self):
        return self.name


mapping_options = [
    MappingEntry(mapping=netflix_mapping_optimized, name="netflix_mapping_optimized"),
    MappingEntry(mapping=netflix_movies_unindexed_fields, name="netflix_movies_unindexed_fields"),
    MappingEntry(
        mapping=netflix_movies_remove_normalisation_factors, name="netflix_movies_remove_normalisation_factors"
    ),
]

if __name__ == "__main__":
    es_connection = EsManagement()
    for m in mapping_options:
        es_connection.create_index(index_name=m.__name__, mapping=m.mapping)
        es_connection.populate_index(index_name=m.__name__, path=os.path.join("../data", "netflix_titles.csv"))
        print(json.dumps(es_connection.es_client.indices.get_mapping(index=m.__name__), indent=1))
