from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True)
    mehbooyeh = db.relationship('mehbooyeh', backref='user', lazy=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

class mehbooyeh(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(140), unique=False, nullable=False)
    creator_id = db.Column(db.Integer, db.ForeignKey('User.id'),
        nullable=False)
    mehs = db.Column(db.Integer)
    boos = db.Column(db.Integer)
    yehs = db.Column(db.Integer)

    def __init__(self, item):
        self.item = item
        self.mehs = 0
        self.boos = 0
        self.yehs = 0
