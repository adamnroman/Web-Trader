#!/usr/bin/env python3
import requests
import json
from flask import render_template

def get_quote(ticker_symbol):
    url = 'http://dev.markitondemand.com/modapis/api/v2/quote/json?symbol={}'.format(ticker_symbol)
    quote = json.loads(requests.get(url).text)
    if 'Message' in quote:
        return quote['Message']
    else:
        return quote['LastPrice']
    
  
