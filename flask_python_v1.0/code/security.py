from werkzeug.security import safe_str_cmp #for string comparisons if needed
from user import User

users = [
    User(1,'Jeff','password'),
    User(2,'Tony','Stark'),
    User(3,'Bruce','Banner'),
    User(4,'Thor','OdinSon'),
    User(5,'John','Rodgers')
]


def authenticate(username, password):
    user = User.find_by_username(username)
    if user and (user.password == password):
        return user

def idendity(payload):
    user_id = payload['identity']
    return User.find_by_id(user_id)
