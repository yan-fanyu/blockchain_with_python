from flask import Flask
from flask_cors import CORS

from wallet import Wallet
from blockchain import Blockchain

app = Flask(__name__)
wallet = Wallet()
blockchain = Blockchain(wallet.public_key)
CORS(app)

@app.route('/', methods=['GET'])
def get_ui():
    return "Hello"

@app.route('/', methods=['GET']):
def get_chain():
    pass

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000)

