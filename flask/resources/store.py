import uuid
from flask import Flask
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import StoreSchema
from models import StoreModel
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from db import db

bp = Blueprint("stores", __name__, description="Operation on stores")

@bp.route("/store/<string:store_id>")
class Store(MethodView):
  @bp.response(200, StoreSchema)
  def get(self, store_id):
    store = StoreModel.query.get_or_404(store_id)
    return store

  def delete(self, store_id):
    store = StoreModel.query.get_or_404(store_id)
    db.session.delete(store)
    db.session.commit()
    return {"message": "Store Deleted"}

  @bp.arguments(StoreSchema)
  @bp.response(200, StoreSchema)
  def put(self, request_data, store_id):
    store = StoreModel.query.get_or_404(store_id)
    if store:
      store.name = request_data["name"]
      db.session.add(store)
      db.session.commit()
    return store

@bp.route("/store")
class StoreList(MethodView):
  @bp.response(200, StoreSchema(many=True))
  def get(self):
    return StoreModel.query.all()

  @bp.arguments(StoreSchema)
  @bp.response(200, StoreSchema)
  def post(self, request_data):
    store = StoreModel(**request_data)

    try:
      db.session.add(store)
      db.session.commit()
    except IntegrityError:
      abort(400, message="Store with that name already exists")      
    except SQLAlchemyError:
      abort(500, message="Something went wrong")

    return store