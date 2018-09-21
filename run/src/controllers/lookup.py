#!/usr/bin/env python3

from flask import Blueprint, render_template, request, session, abort

controller = Blueprint('lookup',__name__)

@controller.route('/lookup',__name__)
def lookup():
    if 'username' in session:
        if request.method == 'POST':
            user_input = request.form['search_input']
            results = get_lookup(user_input)
            return render_template('results.html', company_name=user_input)
    else:
        abort(403)