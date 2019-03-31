from app import db



Class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80), unique = True, nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)


Class Item(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(120), nullable = False)
    location = db.Column(db.String(120), nullable = False)
    lostBy = db.Column(db.Integer, db.ForeignKey('User.id'), nullable = False)
    active = db.Column(db.Boolean, default = True, nullable = False)
    date = db.Column(db.DateTime, nullable = False)

Class Lost(Item):
    pass

Class Found(Item):
    pass
