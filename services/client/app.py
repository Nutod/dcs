from pyfiglet import Figlet
import os
from flask import Flask, request, render_template, jsonify
import binascii
from collections import OrderedDict

font = Figlet(font="starwars")


app = Flask(__name__)

print(font.renderText('SERVER RUNNING...'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/make/transaction')
def make_transaction():
    return render_template('make_transaction.html')

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