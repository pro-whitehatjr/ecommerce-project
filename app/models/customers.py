from app import db
import uuid

from app.models.orders import Orders

class Customers(db.Model):
    __tablename__ = "customers"
    id = db.Column(db.Integer, primary_key=True)
    guid = db.Column(db.String, nullable=False, unique=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    company_name = db.Column(db.String)
    address = db.Column(db.String)
    city = db.Column(db.String)
    county = db.Column(db.String)
    state = db.Column(db.String)
    zip_code = db.Column(db.String)
    phone_1 = db.Column(db.String)
    phone_2 = db.Column(db.String)
    email = db.Column(db.String)
    web = db.Column(db.String)
    orders = db.relationship(Orders, lazy=True, backref="user")

    @staticmethod
    def create(id, first_name, last_name, company_name, address, city, county, state, zip_code, phone_1, phone_2, email, web):
        try:
            customer_dict = dict(
                id = id,
                guid = str(uuid.uuid4()),
                first_name = first_name,
                last_name = last_name,
                company_name = company_name,
                address = address,
                city = city,
                county = county,
                state = state,
                zip_code = zip_code,
                phone_1 = phone_1,
                phone_2 = phone_2,
                email = email,
                web = web
            )
            customer_obj = Customers(**customer_dict)
            db.session.add(customer_obj)
            db.session.commit()
        except:
            db.session.rollback()
            pass