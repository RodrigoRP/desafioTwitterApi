from ingestion import DataIngestor


def main():
    search_words = 'boticario'
    table_name = "tbl_tweets"

    DataIngestor(
        search_words,
        table_name
    )


if __name__ == "__main__":
    main()
