from flask_restful import Resource
from models.store import StoreModel


class Store(Resource):

    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        else:
            return {'message': 'Store not available'}, 404

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message': "Store '{}' already exists".format(name)}, 400  # format(name) replaces curly brackets...
                                                                               # ...with store name
        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {'message': 'Error occured while creating store name'}, 500

        return store.json(), 201

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()

        return {'message': 'Store deleted!'}


class StoreList(Resource):
    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}
