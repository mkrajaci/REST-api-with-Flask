from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        'name': 'My store',
        'items': [
            {
                'name': 'My item',
                'price': 15.99
            }
        ]
    }
]


# POST /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)


# GET /store/<string:name> 
@app.route('/store/<string:name>')
def get_store(name):
    # Iterate over stores
    for store in stores:
        # If the store name matches, return it
        if store['name'] == name:
            return jsonify(store)
        # If none match, return an error message
        else:
            return jsonify({'message': 'store not found'})
    pass


# GET /store 
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})


# POST /store/<string:name>/item {name:, price:} 
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['items'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
        else:
            return jsonify({'message': 'store not found'})


# GET /store/<string:name>/item 
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    for store in stores:
        if store['items'] == name:
            return jsonify({'items': store['items']})
        else:
            return jsonify({'message': 'item not found'})


app.run(port=5000)
