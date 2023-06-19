import pytrends
from urllib.parse import quote
import pandas as pd 
from pytrends.request import TrendReq

pytrend_ins = TrendReq(hl='vi', 
                       tz=420, 
                       geo='VN',
                       proxies=[])

def keyword_suggestion(keyword):
    suggestions_dict = pytrend_ins.suggestions(keyword=keyword)
    return [i['title'] for i in suggestions_dict]


