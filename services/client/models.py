import datetime
from app import db


class Transaction(db.Model):

    __tablename__ = 'transactions'

    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String, nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    recipient = db.Column(db.String, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False)

    def __init__(self, sender, amount, recipient):
        self.sender = sender
        self.amount = amount
        self.recipient = recipient
        self.date_posted = datetime.datetime.now()