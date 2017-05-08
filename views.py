from flask import Blueprint

hello_page = Blueprint('hello_page', __name__, template_folder='templates')

@hello_page.route('/')
def hello_world():
    return "Hello, world!"
