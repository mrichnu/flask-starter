import unittest
import flask_testing
from application import app, db
from manage import do_init_db, do_reset_db
from models import User

class InitialTestCase(flask_testing.TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        return app

    def setUp(self):
        do_init_db()

    def tearDown(self):
        db.session.remove()
        do_reset_db()

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual('200 OK', response.status)
        self.assertTrue('Hello, world' in response.data.decode())

    def test_user_count_no_users(self):
        response = self.client.get('/usercount')
        self.assertEqual('200 OK', response.status)
        self.assertTrue('There are 0 users' in response.data.decode())

    def test_user_count_one_user(self):
        db.session.add(User(username='test', email='test@test.com'))
        db.session.commit()
        response = self.client.get('/usercount')
        self.assertEqual('200 OK', response.status)
        self.assertTrue('There are 1 users' in response.data.decode())

if __name__ == '__main__':
    unittest.main()
