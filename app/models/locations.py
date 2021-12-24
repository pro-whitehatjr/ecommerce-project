from app import db
import uuid

class Locations(db.Model):
    __tablename__ = "locations"
    id = db.Column(db.Integer, primary_key=True)
    guid = db.Column(db.String, nullable=False, unique=True)
    name = db.Column(db.String)
    address = db.Column(db.String)
    city = db.Column(db.String)
    country = db.Column(db.String)
    pin_code = db.Column(db.String)
    rating = db.Column(db.Integer)
    price = db.Column(db.Integer)
    image = db.Column(db.String)

    @staticmethod
    def create(name, address, city, country, pin_code, rating, price, image):
        location_dict = dict(
            guid = str(uuid.uuid4()),
            name = name,
            address = address,
            city = city,
            country = country,
            pin_code = pin_code,
            rating = rating,
            price = price,
            image = image
        )
        location_obj = Locations(**location_dict)
        db.session.add(location_obj)
        db.session.commit()