import uuid
from flask import Flask
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import ItemSchema, ItemUpdateSchema
from models import ItemModel
from db import db
from sqlalchemy.exc import SQLAlchemyError

bp = Blueprint("items", __name__, description="Operation on items")

@bp.route("/item/<string:item_id>")
class Item(MethodView):
  @bp.response(200, ItemSchema)
  def get(self, item_id):
    item = ItemModel.query.get_or_404(item_id)
    return item;

  def delete(self, item_id):
    item = ItemModel.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return {"message": "Item deleted"}

  @bp.arguments(ItemUpdateSchema)
  @bp.response(200, ItemSchema)
  def put(self, request_data, item_id):
    item = ItemModel.query.get_or_404(item_id)
    if item:
      item.price = request_data["price"]
      item.name = request_data["name"]
      db.session.add(item)
      db.session.commit()

    return item

@bp.route("/item")
class ItemList(MethodView):
  @bp.response(200, ItemSchema(many=True))
  def get(self):
    items = ItemModel.query.all()
    return items

  @bp.arguments(ItemSchema)
  @bp.response(201, ItemSchema)
  def post(self, request_data):
    item = ItemModel(**request_data)

    try:
      db.session.add(item)
      db.session.commit()

    except SQLAlchemyError:
      abort(500, message="Something went wrong")

    return item