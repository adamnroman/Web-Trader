#!/usr/bin/env python3

from .orm import Database
from flask import Flask, render_template, redirect

def login(username,password):
    with Database('web.db') as db:
        db.cursor.execute("""SELECT password FROM users WHERE username=?;""",(username,))
        #remember password2 is a tuple with one object
        password2 = db.cursor.fetchone()
        if password2:
            if password == password2[0]:
                #TODO change success page to the main menu
                return redirect('http://127.0.0.1:5001/main')
            #TODO login failure html has to be the login page with 'loginfailure' on it
            return render_template('login_failure.html')
        return render_template('login_failure.html')
