from flask import Blueprint, render_template, session, redirect, url_for, request, jsonify

from app import db

views = Blueprint('views', __name__, url_prefix="/")

@views.route("/editor")
def editor():
    try:
        return render_template("/editor/editor.html")
    except Exception as e:
        return jsonify({
            "message": str(e),
            "status": "error"
        }), 400