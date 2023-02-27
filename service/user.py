import base64
import hashlib
import hmac

from dao.user import UserDAO
from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_by_username(self, username):
        return self.dao.get_by_username(username)

    def get_all(self):
        return self.dao.get_all()

    def create(self, user_data):
        user_data['password'] = self.generate_hash(user_data['password'])
        return self.dao.create(user_data)

    def update(self, user_data):
        user_data['password'] = self.generate_hash(user_data['password'])
        self.dao.update(user_data)

    def delete(self, uid):
        self.dao.delete(uid)

    def generate_hash(self, password):
        password_digest = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )
        return base64.b64encode(password_digest)

    def compare_passwords(self, hash_password, password):
        decoded_digest = base64.b64decode(hash_password)

        password_digest = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )

        return hmac.compare_digest(decoded_digest, password_digest)