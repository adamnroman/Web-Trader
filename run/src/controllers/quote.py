#!/usr/bin/env python3

from flask import Blueprint, render_template, request, session, abort
from src.models.quote import get_quote

controller = Blueprint('quote', __name__)

@controller.route('/quote', methods=['GET','POST'])
def quote():
    if 'username' in session:
        if request.method == 'POST':
            # use jinja here to render template with stock and quote
            ticker_symbol = request.form['ticker_symbol']
            quote = get_quote(ticker_symbol)
            return render_template('quote.html',quote_variable=quote,user_inp=ticker_symbol)
        return render_template('quote.html',quote_variable=None,user_inp=None)
    else:
        abort(403)