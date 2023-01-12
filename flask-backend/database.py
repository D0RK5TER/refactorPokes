from dotenv import load_dotenv
load_dotenv()
from app import app, db
from app.models import Pokemon, Item


with app.app_context():
    db.drop_all()
    db.create_all()

    for i in range(1,20):
        pokemon = Pokemon(number= i, attack = i*2, defense = i+2,
        image_url="https://www.google.com/url?sa=i&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FDexter_%2528season_2%2529&psig=AOvVaw2ziyZoeBYdBuf1RuC2BGct&ust=1673647948988000&source=images&cd=vfe&ved=0CA8QjRxqFwoTCOiH9dCGw_wCFQAAAAAdAAAAABAD",
        name = f"Dexter {i}", type= "fire", moves="Dunk", encounter_rate=i+5, catch_rate= i+11, captured= i%2==0)
        db.session.add(pokemon)
        for o in range(1,10):
            item = Item(happiness= o, image_url = "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.imdb.com%2Ftitle%2Ftt0773262%2F&psig=AOvVaw2ziyZoeBYdBuf1RuC2BGct&ust=1673647948988000&source=images&cd=vfe&ved=0CA8QjRxqFwoTCOiH9dCGw_wCFQAAAAAdAAAAABAJ",
            name= "Dexter's Item" + str(o), price = o*2, pokemon_id = i)
            db.session.add(item)
    db.session.commit()
