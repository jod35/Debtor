from . import db
from . import login_manager


class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(40), nullable=False, unique=True)
    email = db.Column(db.String(80), nullable=False, unique=True)
    pass_hash = db.Column(db.Text, nullable=False)

    def __init__(self, name, username, email, pass_hash):
        self.name = name
        self.username = username
        self.email = email
        self.pass_hash = pass_hash

    def __repr__(self):
        return "{}".format(self.username)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
