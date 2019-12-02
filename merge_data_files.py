import pandas as pd
from datetime import datetime, timedelta


def list_diff(list1, list2):
    """"
    returns list1 - list2 and list2 - list1
    to find difference between 2 lists.
    """
    l1_l2 = []
    l2_l1 = []
    for ele in list1:
        if not ele in list2:
            l1_l2.append(ele)

    for ele in list2:
        if not ele in list1:
            l2_l1.append(ele)

    return l1_l2, l2_l1


def merge_crypto_gnews_sentiment(crypto_data_filename, google_news_data_filename, output_data_filename):
    """

    News data is per day, and crypto data is per hour.
    So news data is replicated 24 times for each hour w.r.t. each day so that it can be concatinated with crypto data

    :param crypto_data_filename:
    :param google_news_data_filename:
    :param output_data_filename:
    :return:
    """
    crypto_df = pd.read_csv(crypto_data_filename, index_col=0)
    crypto_df.index = pd.to_datetime(crypto_df.index)
    news_df = pd.read_csv(google_news_data_filename, index_col=0)

    ilist = [str(d) for d in news_df.index]
    hr1 = timedelta(hours=1)
    news_col = list(news_df.columns)
    news_df_comb = pd.DataFrame(columns=news_col)

    for ilist_index, ilist_item in enumerate(ilist):
        dt = datetime.strptime(ilist_item, '%Y-%m-%d')
        for hr_ in range(0, 24):
            row_id_new = dt.strftime('%Y-%m-%d %H:00:00')
            row_id_value = news_df.loc[ilist_item]
            dt += hr1
            news_df_comb.loc[row_id_new] = row_id_value
    news_df_comb.index.name = 'timestamp'
    news_df_comb.to_csv(google_news_data_filename[0:-4] + '_with_timestamp.csv')
    result = pd.concat([crypto_df, news_df_comb], axis=1)
    result.to_csv(output_data_filename)

    return True


def merge_crypto_gnews_reddit_sentiment(crypto_gnews_filename, reddit_data_filename, crypto_gnews_reddit_filename):
    crypto_gnews_df = pd.read_csv(crypto_gnews_filename, index_col=0)
    reddit_df = pd.read_csv(reddit_data_filename, index_col=0)
    result = pd.concat([crypto_gnews_df, reddit_df], axis=1)
    result.to_csv(crypto_gnews_reddit_filename)


if __name__ == '__main__':
    crypto_data_filename = 'crypto_data_master_cleaned.csv'
    gnews_data_filename = 'google_news_final_sentiment.csv'
    crypto_gnews_filename = 'crypto_data_news_final.csv'
    reddit_data_filename = 'reddit_data_sentiment_bucketized.csv'
    crypto_gnews_reddit_filename = 'crypto_data_news_reddit_final.csv'
    merge_crypto_gnews_sentiment(crypto_data_filename, gnews_data_filename, crypto_gnews_filename)
    merge_crypto_gnews_reddit_sentiment(crypto_gnews_filename, reddit_data_filename, crypto_gnews_reddit_filename)
