from app import app
from db import db

db.init_app(app)


@app.before_first_request
def create_tables():   # This allows SQLAlchemy to create tables automatically
    db.create_all()