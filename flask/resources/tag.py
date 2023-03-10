from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import TagModel, StoreModel, ItemModel
from schemas import TagSchema, TagAddItems

bp = Blueprint("tags", __name__, description="Operation on tags")

@bp.route("/store/<string:store_id>/tag")
class TagInStore(MethodView):
  @bp.response(200, TagSchema(many=True))
  def get(self, store_id):
    store = StoreModel.query.get_or_404(store_id)

    return store.tags,all()

  @bp.arguments(TagSchema)
  @bp.response(201, TagSchema)
  def post(self, tag_data, store_id):
    if TagModel.query.filter(TagModel.store_id == store_id, TagModel.name == tag_data["name"]).first():
      abort(400, message="A tag with that name already exists in that store.")
    tag = TagModel(**tag_data, store_id=store_id)

    try:
      db.session.add(tag)
      db.session.commit()
    except SQLAlchemyError as e:
      abort(500, message=str(e))
    
    return tag

@bp.route("/item/<string:item_id>/tag/<string:tag_id>")
class LinkTagsToItem(MethodView):
  @bp.response(201, TagSchema())
  def post(self, item_id, tag_id):
    item = ItemModel.get_or_404(item_id)
    tag = TagModel.get_or_404(tag_id)
    item.tags.append(tag)

    try:
      db.session.add(item)
      db.session.commit()
    except:
      abort(500, message="Some error occured")
    return tag

  @bp.response(200, TagAddItems())
  def post(self, item_id, tag_id):
    item = ItemModel.get_or_404(item_id)
    tag = TagModel.get_or_404(tag_id)
    item.tags.remove(tag)

    try:
      db.session.add(item)
      db.session.commit()
    except:
      abort(500, message="Some error occured")
    return {"message": "Item removed from tag", "item": item, "tag": tag}

@bp.route("/tag/<string:tag_id>")
class Tag(MethodView):
  @bp.response(200, TagSchema)
  def get(self, tag_id):
    tag = TagModel.query.get_or_404(tag_id)
    return tag

  @bp.response(202, description="Deletes a tag if no item is tagged with it")
  @bp.alt_response(404, description="Tag not found")
  @bp.alt_response(400, description="The tag is assigned to one or more items")
  def delete(self, tag_id):
    tag = TagModel.query.get_or_404(tag_id)
    
    if not tags.items:
      db.session.delete(tag)
      db.session.commit()
      return {"message": "Tag deleted"}
    abort(400, message="Tag is assigned to some items, so cannot delete it")