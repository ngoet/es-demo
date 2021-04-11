netflix_mapping = {
    "mappings": {
        "properties": {
            "show_id": {"type": "text"},
            "type": {"type": "text"},
            "title": {"type": "text"},
            "director": {"type": "text"},
            "cast": {"type": "text"},
            "country": {"type": "text"},
            "date_added": {"type": "text"},
            "release_year": {"type": "integer"},
            "rating": {"type": "text"},
            "duration": {"type": "text"},
            "listed_in": {"type": "text"},
            "description": {"type": "text"},
        }
    }
}

netflix_mapping_optimized = {
    "mappings": {
        "properties": {
            "show_id": {"type": "text"},
            "type": {"type": "keyword"},
            "title": {"type": "text"},
            "director": {"type": "text"},
            "cast": {"type": "text"},
            "country": {"type": "keyword"},
            "date_added": {"type": "text"},
            "release_year": {"type": "short"},
            "rating": {"type": "keyword"},
            "duration": {"type": "text"},
            "listed_in": {"type": "text"},
            "description": {"type": "text"},
        }
    }
}
