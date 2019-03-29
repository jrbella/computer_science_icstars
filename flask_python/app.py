from flask import Flask

app = Flask(__name__)

# POST /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
    pass

# GET /store/<string:name>
@app.route('/store/<string:name>', methods=['GET'])
def get_store(name):
    pass

# GET /store/<string:name>/item
@app.route('/store/<string:name>/item', methods=['GET'])
def get_store(name):
    pass

# POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def get_store(name):
    pass

app.run(port=5000)

