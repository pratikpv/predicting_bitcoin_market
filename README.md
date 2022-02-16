# Predictive analysis of Bitcoin price considering social sentiments.

# ABSTRACT

We report on the use of sentiment analysis on news and social media to analyze and predict the price of
Bitcoin. Bitcoin is the leading cryptocurrency and has the highest market capitalization among digital
currencies. Predicting Bitcoin values may help understand and predict potential market movement and
future growth of the technology. Unlike (mostly) repeating phenomena like weather, cryptocurrency
values do not follow a repeating pattern and mere past value of Bitcoin does not reveal any secret of
future Bitcoin value. Humans follow general sentiments and technical analysis to invest in the market.
Hence considering people’s sentiment can give a good degree of prediction. We focus on using social
sentiment as a feature to predict future Bitcoin value, and in particular, consider Google News and
Reddit posts. We find that social sentiment gives a good estimate of how future Bitcoin values may
move. We achieve the lowest test RMSE of 434.87 using an LSTM that takes as inputs the historical price of various cryptocurrencies, the sentiment of news articles and the sentiment of Reddit posts.

**KEYWORDS**

Bitcoin · Bitcoin price prediction · Cryptocurrency · Blockchain · Machine learning · Artificial intelligence ·
Long short-term memory (LSTM) · Gated recurrent unit (GRU) · Convolution neural network (CNN) · Sentiment
analysis.

# Introduction

Bitcoin has sparked a gigantic interest in cryptocurrency and blockchain technology. Since the inception of Bitcoin,
cryptocurrency has gained the trust of the general population. Bitcoin has achieved the highest market capitalization
among all of the cryptocurrencies. As of this writing Bitcoin market capitalization is more than 134 billion US dollars.
Bitcoin gains this market value as there a huge demand for this cryptocurrency. The demand for the cryptocurrency
directly translates into people’s trust in the Bitcoin and the underneath technology. Since people’s trust is involved in
the rise of the cryptocurrency market, the sentiment of the general population does make a huge impact on the future of
the cryptocurrency market capitalization. Hence, we use the sentiment of people in an attempt to predict future Bitcoin
prices. https://news.google.com (Google News) is a nice source for collecting news posted by various journalists around
the globe. Google News also provides the capability to search the news based on selected keywords and its search tools
also have a feature of crawling the news based on the date of the news release. While Google News gives opinions
of the various journalists we also focus on sentiments of the general population. https://www.Reddit.com (Reddit) is
also one of the most famous social platforms where people can post anonymously. We also consider the sentiment of
messages posted on Reddit to predict the Bitcoin price movement. Along with sentiments, we have included historical
price and volume of Litecoin and Ethereum. We have trained various machine learning models to learn about the
correlation between all these features and results are analyzed

# Overall Goal

<img src="https://github.com/pratikpv/predicting_bitcoin_market/blob/master/images/model_arch.png" width=70% height=90%>

# Results for best performing model (Expriment# 4)

<img src="https://github.com/pratikpv/predicting_bitcoin_market/blob/master/images/expr4_results.png" width=70% height=90%>

# Note

Please cite my paper https://arxiv.org/abs/2001.10343 if you want to use the code posted in this repository or any code referenced by this code-base and authored by me.


**How to cite!**

```
@misc{prajapati2020predictive,
    title={Predictive analysis of Bitcoin price considering social sentiments},
    author={Pratikkumar Prajapati},
    year={2020},
    eprint={2001.10343},
    archivePrefix={arXiv},
    primaryClass={cs.IR}
}
```
#
