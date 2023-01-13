# from flask import render_template
# # from ..db_jokes import jokes
# # from ..forms.joke_form import NewJokeForm
# from ..models import db, Pokemon, Item
# from random import randint
# from flask import render_template

# from app import app


# @app.route('/')
# def all_pokemon():
#     pokemon = Pokemon.query.all()
#     base = '<div>'
#     for p in pokemon:
#         base += p.name
#     return render_template(base + '</div>')


# @app.route('/types')
# def pokemon_types():

#     types = list("fire"
#                  "electric"
#                  "normal"
#                  "ghost"
#                  "psychic"
#                  "water"
#                  "bug"
#                  "dragon"
#                  "grass"
#                  "fighting"
#                  "ice"
#                  "flying"
#                  "poison"
#                  "ground"
#                  "rock"
#                  "steel")
#     base = '<div>'
#     for t in types:
#         base += f'<p>{t}</p>'
#     return render_template(base + '</div>')


# @app.route('/random')
# def random_poke():
#     pokemon = Pokemon.query.get(randint(0, len(Pokemon.query.all())))
#     return render_template(f"<h1>{pokemon.name}</h1>")

# # @app.route('/battle')
# # def battle():
# #     allies =


# @app.route('/<int:id>')
# def one_pokemon(id):
#     pokemon = Pokemon.query.get(id)
#     return render_template(f"<h1>{pokemon.name}</h1>")


# @app.route('/<int:id>/items')
# def one_pokemon(id):
#     pokemon_items = Item.query.get(pokemon_id=id).all()

#     base = '<div>'
#     for t in pokemon_items:
#         base += f'<p>{t}</p>'
#     return render_template(base + '</div>')

#     # return render_template(f"<h1>{pokemon.items}</h1>")
