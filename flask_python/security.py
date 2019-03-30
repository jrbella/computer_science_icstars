from werkzeug.security import safe_str_cmp #for string comparisons if needed
from user import User

users = [
    User(1,'Jeff','password'),
    User(2,'Tony','Stark'),
    User(3,'Bruce','Banner'),
    User(4,'Thor','OdinSon'),
    User(5,'John','Rodgers')
]

username_mapping = {u.username: u for u in users}
userid_mapping = {u.id: u for u in users}


def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user and (user.password == password):
        return user

def idendity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)
