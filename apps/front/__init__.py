from flask import Blueprint

front = Blueprint('front',__name__,url_prefix='/front')

import apps.front.views