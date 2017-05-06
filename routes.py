"""
Routes and views for the bottle application.
"""

from bottle import route, view, response
from datetime import datetime
from random import randint


@route('/')
@route('/home')
@view('index')
def home():
    """Renders the home page."""
    return dict(
        year=datetime.now().year
    )

@route('/api-request')
def returnarray():
	rv = [{ "id": 1, "random": randint(1000,9999)}, { "id": 2, "random": randint(1000,9999) }]
	return dict(data=rv)
