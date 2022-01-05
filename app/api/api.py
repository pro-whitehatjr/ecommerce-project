from flask import Blueprint, jsonify, request, session, redirect, url_for, send_file

from werkzeug.utils import secure_filename
from app import db
import os

api = Blueprint('api', __name__, url_prefix="/api")

UPLOAD_FOLDER = os.path.abspath("app/static/attachments")

@api.route("/execute", methods=["POST"])
def execute():
    try:
        code = request.json.get("code")
        result = db.engine.execute(code).all()
        if len(result) == 0:
            return jsonify({
                "status": "no_result"
            }), 200
        else:
            keys, values = result[0].keys()._keys, []
            for result_obj in result:
                temp_values = []
                for result_value in result_obj:
                    temp_values.append(result_value)
                values.append(temp_values)
            return jsonify({
                "status": "success",
                "keys": keys,
                "values": values
            }), 200
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 400

@api.route("/get-customer")
def get_customer():
    try:
        customer_id = request.args.get("id")
        query = f"select * from customers where id={customer_id}"
        customer = db.engine.execute(query).first()
        return jsonify({
            "status": "success",
            "data": {
                "first_name": customer["first_name"],
                "last_name": customer["last_name"],
                "company_name": customer["company_name"],
                "address": customer["address"],
                "city": customer["city"],
                "county": customer["county"],
                "state": customer["state"],
                "zip_code": customer["zip_code"],
                "phone_1": customer["phone_1"],
                "phone_2": customer["phone_2"],
                "email": customer["email"],
                "web": customer["web"]
            }
        }), 200
    except Exception as e:
        return jsonify({
            "status", "error",
            "message": str(e)
        }), 400