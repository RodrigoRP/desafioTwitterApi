import pandas as pd

from cleaners import clean_text
from readerApi import get_list_tweets


def create_df(list_tweets):
    return pd.DataFrame(data=list_tweets, columns=['usuario', "localizacao", "mensagem"])


def read_dataframe(new_search):
    list_tweets = get_list_tweets(new_search)
    df = create_df(list_tweets)
    df['mensagem'].apply(clean_text)
    return df


def get_best_selling(conn):
    sql_query = "select linha, count(qtd_venda) as total from tbl_vendas group by linha order by total desc limit 1;"
    df = pd.read_sql(sql_query, conn)
    return df['linha'].values[0]
