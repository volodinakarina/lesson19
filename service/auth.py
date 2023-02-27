import calendar
import datetime
import jwt

from flask import current_app, abort
from constants import JWT_ALGO, DELTA_MINS, DELTA_DAYS
from service.user import UserService


class AuthService:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def generate_tokens(self, username, password, is_refresh=False):
        user = self.user_service.get_by_username(username)

        if user is None:
            abort(404)

        if not is_refresh:
            if not self.user_service.compare_passwords(user.password, password):  # user_password - hash from the db
                abort(400)

        data = {
            "username": user.username,
            "role": user.role
        }

        delta_min = datetime.datetime.now() + datetime.timedelta(minutes=DELTA_MINS)
        delta_max = datetime.datetime.now() + datetime.timedelta(days=DELTA_DAYS)

        data['exp'] = calendar.timegm(delta_min.timetuple())
        access_token = jwt.encode(data, current_app.config['SECRET_HERE'], algorithm=JWT_ALGO)

        data['exp'] = calendar.timegm(delta_max.timetuple())
        refresh_token = jwt.encode(data, current_app.config['SECRET_HERE'], algorithm=JWT_ALGO)

        return {
            'access_token': access_token,
            'refresh_token': refresh_token
        }

    def approve_refresh_token(self, refresh_token):
        data = jwt.decode(refresh_token, current_app.config['SECRET_HERE'], algorithms=JWT_ALGO)
        username = data.get('username')

        return self.generate_tokens(username, None, is_refresh=True)
