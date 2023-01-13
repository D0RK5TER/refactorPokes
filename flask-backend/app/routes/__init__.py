from flask import Blueprint, render_template, redirect
from
# from ..forms import Items
import math

bp = Blueprint('pokemon',__name__,'')

@bp.route("/<int:id>", methods=['PUT'])
def item_put(id):
    form = tempform()
    if form.validate_on_submit():
        data = Items()
        form.populate_obj(data)
        db.session.add(data)
        item = Item.query.get(id)
        db.session.delete(item)
        db.session.commit()
        return redirect('/')

    return 'Bad Data'

@bp.route("/<int:id>", methods=['DELETE'])
def item_delete(id):
    ite = Item.query.get(id)
    db.session.delete(item)
    db.session.commit()

def randomItemImage():
    images =  [
    "/images/pokemon_berry.svg",
    "/images/pokemon_egg.svg",
    "/images/pokemon_potion.svg",
    "/images/pokemon_super_potion.svg",
  ]
  index = math.floor(math.random() * len(images))
  return images[index]

