import os
from pyfiglet import Figlet
from flask import Flask
from flask import request, redirect, url_for, render_template, jsonify
from pymongo import MongoClient
from bson.json_util import dumps

client = MongoClient('mongodb://mongo:27017/')
db = client.tmptransactions

font = Figlet(font="starwars")


app = Flask(__name__)
print(font.renderText('SERVER RUNNING...'))

print(db)

@app.route('/', methods=['GET'])
def index():   
    _transactions = db.tmptransactions.find().limit(10)
    transactions = [transaction for transaction in _transactions]

    return render_template('index.html', transactions=transactions)


@app.route('/make/transaction', methods=['POST'])
def make_transaction():
    transaction_doc = {
        'senderPublicKey': request.form['senderPublicKey'],
        'recipientAddress': request.form['recipientAddress'],
        'amount': request.form['amount']
    }

    db.tmptransactions.insert_one(transaction_doc)

    return redirect(url_for('index'))

@app.route('/generate/transaction', methods=['POST'])
def generate_transaction():
    pass


@app.route('/view/transactions')
def view_transactions():
    return render_template('view_transactions.html')


@app.route('/wallet/new')
def new_wallet():
    pass


if __name__ == '__main__':
   from argparse import ArgumentParser

   parser = ArgumentParser()
   parser.add_argument('-p', '--port', default=8080, type=int, help='Port to listen from')
   args = parser.parse_args()
   port = args.port

   app.run(host='127.0.0.1', port=port, debug=True)