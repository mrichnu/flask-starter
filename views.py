from flask import request, session
from application import app
from models import User

@app.route('/')
def hello_world():
    visit_count = session.get('visit_count', 0)
    visit_count += 1
    session['visit_count'] = visit_count
    return "Hello, world! You are using {0}.<br />I have seen you {1} times.".\
            format(request.headers['User-Agent'], visit_count)

@app.route('/usercount')
def user_count():
    user_count = User.query.count()
    return "Hello, world! There are {0} users in the database.".\
            format(user_count)
