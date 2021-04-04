from es_connection import EsManagement


if __name__ == "__main__":
    es_connection = EsManagement()
    es_connection.populate_index(index_name="netflix_movies", path=os.path.join("data", "netflix_titles.csv"))
