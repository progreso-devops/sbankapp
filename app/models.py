from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String(150), nullable=False)
    branch_name = db.Column(db.String(150), nullable=False)
    mobile = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    from_account = db.Column(db.String(150), nullable=False)
    to_account = db.Column(db.String(150), nullable=False)
    remarks = db.Column(db.String(300), nullable=False)

