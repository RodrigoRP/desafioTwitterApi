from authenticators import authentication_db
from cleaners import clean_tbl_name, replace_dtype
from databaseFun import connect_db, create_table, execute_values
from dataframeFun import read_dataframe, get_best_selling


class DataIngestor:

    def __init__(self, search_words, tbl_name) -> None:
        self.search_words = search_words,
        self.tbl_name = tbl_name
        self._get_twitter_api = self._get_twitter_api()

    def _get_twitter_api(self):
        tbl_name = self.tbl_name
        search_words = self.search_words

        # Database
        param_dic = authentication_db()
        conn = connect_db(param_dic)

        # Get name line better sell
        line_best = get_best_selling(conn)

        # Concatenate search_words and line_best
        search_words = str(search_words) + line_best

        # Clean table name
        tbl_name = clean_tbl_name(tbl_name)

        # Read CSV - Create DF
        df = read_dataframe(search_words)

        # Replace columns dtypes
        col_str = replace_dtype(df)

        # Create table database
        create_table(conn, tbl_name, col_str)

        # Insert tweets database
        execute_values(conn, df, tbl_name)

        print(get_best_selling(conn))

        conn.close()
