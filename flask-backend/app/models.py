from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
import enum
from sqlalchemy import Enum

class MyEnum(enum.Enum):

  fire = "fire"
  electric = "electric"
  normal = "normal"
  ghost = "ghost"
  psychic = "psychic"
  water = "water"
  bug = "bug"
  dragon = "dragon"
  grass = "grass"
  fighting = "fighting"
  ice = "ice"
  flying = "flying"
  poison = "poison"
  ground = "ground"
  rock = "rock"
  steel = "steel"



db = SQLAlchemy()
UNKNOWN_IMG_URL = "/images/unknown.png"

class Pokemon(db.Model):
    __tablename__= "pokemons"
    id = db.Column(db.Integer, primary_key =True)
    number = db.Column(db.Integer, nullable=False, unique=True)
    attack = db.Column(db.Integer, nullable=False)
    defense = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False, unique=True)
    type = db.Column(Enum(MyEnum), nullable=False, )
    moves = db.Column(db.String, nullable=False)
    encounter_rate = db.Column(db.DECIMAL(3,2))
    catch_rate = db.Column(db.DECIMAL(3,2))
    captured = db.Column(db.Boolean)
    items = db.relationship("Item", back_populates="pokemon")






    @validates("number")
    def validation_number(self, key, pokemons):
        if pokemons < 1:
            raise ValueError("Number has to be greater than 1")
        return pokemons
    @validates("attack")
    def validation_attack(self, key, pokemons):
        if pokemons < 0 or pokemons > 100:
            raise ValueError("Defense has to be between 0 and 100")
        return pokemons
    @validates("defense")
    def validation_defense(self, key, pokemons):
        if pokemons < 0 or pokemons > 100:
            raise ValueError("Defense has to be between 0 and 100")
        return pokemons
    @validates("name")
    def validation_name(self, key, pokemons):
        if len(pokemons) < 3 or len(pokemons) > 255:
            raise ValueError("Name must be between 3 and 255 characters")
        return pokemons

    @validates("encounter_rate")
    def validation_encounter_rate(self, key, pokemons):
        if pokemons < 0 or pokemons > 100:
            raise ValueError("encounter_rate has to be between 0 and 100")
        return pokemons
    @validates("catch_rate")
    def validation_catch_rate(self, key, pokemons):
        if pokemons < 0 or pokemons > 100:
            raise ValueError("catch_rate has to be between 0 and 100")
        return pokemons

    # define get image url method
    @property
    def get_img_url(self):
        captured = self.captured
        if (captured):
            return self.image_url
        return UNKNOWN_IMG_URL

    # get and set methods for moves
    @property
    def get_moves(self):
        rawValue = self.moves
        if rawValue:
            return rawValue
        else:
            return None

    @get_moves.setter
    def set_moves(self, moves):
        self.moves = moves

class Item(db.Model):
    __tablename__= "items"
    id = db.Column(db.Integer, primary_key =True)
    happiness = db.Column(db.Integer)
    image_url = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.String, nullable=False)
    pokemon_id = db.Column(db.Integer, db.ForeignKey("pokemons.id"), nullable=False)
    pokemon = db.relationship("Pokemon", back_populates="items")
