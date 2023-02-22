import uuid
from flask import Flask, request
from flask_smorest import abort
from db import items, stores

app = Flask(__name__)

@app.get("/store")
def get_stores():
  return {"stores": list(stores.values())}

@app.post("/store")
def create_store():
  request_data = request.get_json()
  if "name" not in request_data :
    return abort(400, message = "Bad request")

  store_id = uuid.uuid4().hex
  new_store = {
    "name": request_data["name"],
    "id": store_id
  }
  stores[store_id] = new_store
  return new_store, 201

@app.get("/item")
def get_items():
  return {"items": list(items.values())}


@app.post("/item")
def create_item():
  request_data = request.get_json()
  if (
    "price" not in request_data or
    "store_id" not in request_data or
    "name" not in request_data
  ):
    return abort(400, message = "Bad request")

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

@app.get("/store/<string:store_id>")
def get_store(store_id):
  try:
    return stores[store_id]
  except KeyError:
    return abort(404, message = "Store not found")

@app.get("/item/<string:item_id>")
def get_item(item_id):
  try:
    return items[item_id]
  except KeyError:
    return abort(404, message = "Item not found")