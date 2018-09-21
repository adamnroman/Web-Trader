#!/usr/bin/env python3

from flask import Blueprint, render_template, redirect, request, session, abort

controller = Blueprint('main_menu', __name__)

@controller.route('/main', methods=['GET','POST'])
def main_menu():
    if 'username' in session:
        if request.method == 'POST':
            #TODO route to buy,sell,view,settings etc pages
            return render_template('main_menu.html')
        return render_template('main_menu.html')
    else:
        abort(403)
