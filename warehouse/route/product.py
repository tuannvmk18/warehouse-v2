import json

from flask import Blueprint
from flask import request
from warehouse.service import product as product_service
from flask import Response

product = Blueprint('product_route', __name__)


@product.get("/")
def get_all():
    return Response(json.dumps(product_service.get_all()), mimetype="application/json")


@product.post("/")
def create_new():
    response = product_service.create(request.get_json())
    return Response(json.dumps(response), mimetype="application/json")


@product.patch("/")
def patch():
    payload = dict(request.json)
    product_id = payload.pop('id', None)
    response = product_service.update(product_id, payload)
    if response is not None:
        return response
    return {
        "message": "error"
    }


@product.delete("/<int:product_id>")
def delete(product_id: int):
    if product_service.delete(product_id):
        return {
            "message": "Success"
        }
    return {
        "message": "Error"
    }
