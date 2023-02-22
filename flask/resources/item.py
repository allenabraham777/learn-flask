import uuid
from flask import Flask
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import stores
from schemas import ItemSchema, ItemUpdateSchema

bp = Blueprint("items", __name__, description="Operation on items")

@bp.route("/item/<string:item_id>")
class Item(MethodView):
  def get(self, item_id):
    try:
      return items[item_id]
    except KeyError:
      return abort(404, message = "Item not found")

  def delete(self, item_id):
    try:
      del items[item_id]
      return {"message": "Item deleted"}
    except KeyError:
      return abort(404, message = "Item not found")

  @bp.arguments(ItemUpdateSchema)
  def put(self, request_data, item_id):
    if item_id not in items:
      return abort(404, message = "Item not found")

    if (
      "price" not in request_data or
      "name" not in request_data
    ):
      return abort(400, message = "Bad request")

    item = items[item_id]
    
    item["name"] = request_data["name"]
    item["price"] = request_data["price"]

    items[item_id] = item

    return item, 200

@bp.route("/item")
class ItemList(MethodView):
  def get(self):
    return {"items": list(items.values())}

  @bp.arguments(ItemSchema)
  def post(self, request_data):
    if request_data["store_id"] not in stores:
      return abort(404, message = "Store not found")

    item_id = uuid.uuid4().hex
    new_item = {
      "name": request_data["name"],
      "store_id": request_data["store_id"],
      "price": request_data["price"],
      "id": item_id
    }
    items[item_id] = new_item
    return new_item, 201