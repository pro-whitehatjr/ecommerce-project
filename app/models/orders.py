from app import db
import uuid

class Orders(db.Model):
    __tablename__ = "orders"
    id = db.Column(db.Integer, primary_key=True)
    guid = db.Column(db.String, nullable=False, unique=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'), nullable=False)
    rooms_booked = db.Column(db.Integer, nullable=False)
    checkin = db.Column(db.Date, nullable=False)
    checkout = db.Column(db.Date, nullable=False)
    billing_amount = db.Column(db.Integer, nullable=False)

    @staticmethod
    def create(customer_id, location_id, rooms_booked, checkin, checkout, billing_amount):
        order_dict = dict(
            guid = str(uuid.uuid4()),
            customer_id = customer_id,
            location_id = location_id,
            rooms_booked = rooms_booked,
            checkin = checkin,
            checkout = checkout,
            billing_amount = billing_amount
        )
        order_obj = Orders(**order_dict)
        db.session.add(order_obj)
        db.session.commit()