from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList
from db import db


from security import authenticate, identity

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///data.db'
app.secret_key = 'Ayo'
api = Api(app)


@app.before_first_request
def create_tables():   # This allows SQLAlchemy to create tables automatically
    db.create_all()


jwt = JWT(app, authenticate, identity)

api.add_resource(ItemList, '/items')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(UserRegister, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')

db.init_app(app)
app.run(port=5000, debug=True)
