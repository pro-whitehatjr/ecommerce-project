from flask.cli import FlaskGroup
from app import create_app, db
from flask import current_app

from datetime import datetime
import random
import csv
import os

from app.models.customers import Customers
from app.models.locations import Locations
from app.models.orders import Orders

from random import randrange
from datetime import timedelta

cli = FlaskGroup(create_app=create_app)

def recreate_db():
	db.drop_all()
	db.create_all()
	db.session.commit()

def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

def seeder():
	with open("app/editor_data/customers.csv", 'r') as f:
		csvreader = csv.reader(f)
		for row in csvreader:
			try:
				Customers.create(random.randint(0, 5000), row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11])
			except:
				pass

	with open("app/editor_data/locations.csv", 'r') as f:
		csvreader = csv.reader(f)
		for row in csvreader:
			try:
				Locations.create(row[0], row[1], row[2], row[3], row[4], int(row[5]), int(row[6]), row[7])
			except:
				pass

	customers = Customers.query.all()
	for customer in customers:
		bookings = random.randint(0, 5)
		for i in range(bookings):
			rooms = random.randint(1, 3)
			days = random.randint(1, 8)
			hotel = random.choice(Locations.query.all())
			d1 = datetime.strptime("1/1/2022", "%d/%m/%Y")
			d2 = datetime.strptime("1/1/2023", "%d/%m/%Y")
			checkin = random_date(d1, d2)
			checkout = checkin + timedelta(days=days)
			billing_amount = hotel.price * rooms * days
			Orders.create(customer.id, hotel.id, rooms, checkin, checkout, billing_amount)

@cli.command()
def rsd():
	# if current_app.config.get('ENV') not in ('development', 'test', 'testing'):
	#   print("ERROR: seed-db only allowed in development and testing env.")
	#   return
	recreate_db()
	seeder()

if __name__ == '__main__':
	cli()
