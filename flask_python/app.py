from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from security import authenticate, idendity


app = Flask(__name__)
api = Api(app)
app.secret_key = 'securestring'

jwt = JWT(app, authenticate, idendity) #/auth endpoint

items = []

class Item(Resource):
    #parser is called by Item.parser.parse_args()
    parser = reqparse.RequestParser()
    parser.add_argument('price',
    type=float,
    required=True,
    help='This field should not be blank'
    )
    @jwt_required()
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        for item in items:
            if item['name'] == name:
                return item
        return ({'item': None}), 200 if item else 404

    @jwt_required()
    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None) is not None:
            return {'message': 'An item with the name {} already exists'.format(name)}, 400
                #following block allows to only allow price to be changed
        data = Item.parser.parse_args()
        item = {'name' : name, 'price' : data['price']}
        items.append(item)
        return item, 201 #201 is for 'created'

    @jwt_required()
    def delete(self, name):
        global items #because of scoping
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'Item {} deleted'.format(name)}

    @jwt_required()
    def put(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        data = Item.parser.parse_args()
        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)
        return item



class ItemList(Resource):
    def get(self):
        return {'items': items}

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run(port=5000, debug=True)
