import pytrends
from urllib.parse import quote
import pandas as pd 
from typing import List
from pytrends.request import TrendReq
import app.utils.config as config

pytrend_ins = TrendReq(hl='vi', 
                       tz=420, 
                       geo='VN',
                       proxies=[])

def keyword_suggestion(keyword: str):
    suggestions_dict = pytrend_ins.suggestions(keyword=keyword)
    return [i['title'] for i in suggestions_dict]


def keyword_ranking(keywords: List[str], timeframe: str = 'day'):
    pytrend_ins.build_payload(keywords, 
                          cat=0, 
                          timeframe=config.TIMEFRAME_CONFIG[timeframe], 
                          geo='VN', 
                          gprop='',
                          )
    df = pytrend_ins.interest_over_time()
    df = df.drop(columns=['isPartial'])
    return df.sum().to_dict()