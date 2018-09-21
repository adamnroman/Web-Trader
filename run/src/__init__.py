#!/usr/bin/env python3

from flask import Flask

from .controllers.login import controller as login_controller
from .controllers.main_menu import controller as main_menu_controller
from .controllers.quote import controller as quote_controller
from .controllers.lookup import controller as lookup_controller

import uuid

omnibus = Flask(__name__)
omnibus.secret_key = str(uuid.uuid4())

omnibus.register_blueprint(login_controller)
omnibus.register_blueprint(main_menu_controller)
omnibus.register_blueprint(quote_controller)
omnibus.register_blueprint(lookup_controller)