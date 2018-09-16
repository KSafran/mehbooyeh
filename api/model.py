from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class mehbooyeh(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140), unique=False, nullable=False)
    item = db.Column(db.String(140), unique=False, nullable=False)
    mehs = db.Column(db.Integer)
    boos = db.Column(db.Integer)
    yehs = db.Column(db.Integer)

    def __init__(self, name, item):
        self.name = name
        self.item = item
        self.mehs = 0
        self.boos = 0
        self.yehs = 0
