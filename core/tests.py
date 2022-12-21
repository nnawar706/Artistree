from django.test import TestCase
from .backends import BaseAuthentication

# Create your tests here.

class AuthenticationTestCase(TestCase):

    def get_backend_auth_class(self):
        return BaseAuthentication()

    def test_login_ok(self):
        auth = self.get_backend_auth_class()
        user = auth.authenticate(username='demo', password='demo')
        self.assertIsNotNone(user)

    def test_login_invalid_fields(self):
        auth = self.get_backend_auth_class()
        user = auth.authenticate(username=None, password=None)
        self.assertIsNone(user)

    def test_login_invalid_username(self):
        auth = self.get_backend_auth_class()
        user = auth.authenticate(username='jfstef', password='asdfasdf')
        self.assertIsNone(user)

    def test_login_invalid_password(self):
        auth = self.get_backend_auth_class()
        user = auth.authenticate(username='demo', password='asdfasdf')
        self.assertIsNone(user)

    def test_login_invalid_token(self):
        auth = self.get_backend_auth_class()
        user = auth.authenticate(username='test', password='test')
        token: str = auth.get_token(user=user)
        self.assertIsNone(token)
        self.assertIsNone(user)

    def test_login_inactive_user(self):
        auth = self.get_backend_auth_class()
        user = auth.authenticate(username='test', password='test')
        self.assertIsNone(user)

    def test_token_valid(self):
        auth = self.get_backend_auth_class()
        user = auth.authenticate(username='demo', password='demo')
        token: str = auth.get_token(user=user)
        self.assertIsNotNone(token)
        self.assertIsNotNone(user)