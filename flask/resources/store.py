import uuid
from flask import Flask
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import stores
from schemas import StoreSchema

bp = Blueprint("stores", __name__, description="Operation on stores")

@bp.route("/store/<string:store_id>")
class Store(MethodView):
  def get(self, store_id):
    try:
      return stores[store_id]
    except KeyError:
      return abort(404, message = "Store not found")

  def delete(self, store_id):
    try:
      del stores[store_id]
      return { "message": "Store deleted" }
    except KeyError:
      return abort(404, message = "Store not found")

  @bp.arguments(StoreSchema)
  def put(self, request_data, store_id):
    if store_id not in stores:
      return abort(404, message = "Store not found")

    if "name" not in request_data :
      return abort(400, message = "Bad request")

    store = stores[store_id]
    
    store["name"] = request_data["name"]

    stores[store_id] = store
    
    return store, 200

@bp.route("/store")
class StoreList(MethodView):
  def get(self):
    return {"stores": list(stores.values())}

  @bp.arguments(StoreSchema)
  def post(self, request_data):
    if "name" not in request_data :
      return abort(400, message = "Bad request")

    store_id = uuid.uuid4().hex
    new_store = {
      "name": request_data["name"],
      "id": store_id
    }
    stores[store_id] = new_store
    return new_store, 201