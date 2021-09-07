import json

from flask import Blueprint
from flask import request
from warehouse.service import product as product_service

product = Blueprint('product_route', __name__)


@product.get("/")
def get_all():
    limit = request.args.get('limit')
    offset = request.args.get('offset')
    return {
        "status_code": 200,
        "products": json.loads(json.dumps(product_service.get_all(limit, offset)))
    }


@product.post("/")
def create_new():
    product_json = product_service.create(request.get_json())
    if product_json is not None:
        return {
            "status_code": 200,
            "product": json.loads(json.dumps(product_json))
        }
    return {
        "status_code": 404,
        "message": "Resource not found"
    }


@product.patch("/")
def patch():
    payload = dict(request.json)
    product_id = payload.pop('id', None)
    product_json = product_service.update(product_id, payload)
    if product_json is not None:
        return {
            "status_code": 200,
            "product": json.loads(json.dumps(product_json))
        }
    return {
        "status_code": 404,
        "message": "Resource not found"
    }


@product.get("/<int:product_id>")
def get_by_id(product_id: int):
    product_json = product_service.get_by_id(product_id)
    if product_json is not None:
        return {
            "status_code": 200,
            "product": json.loads(json.dumps(product_json))
        }
    return {
        "status_code": 404,
        "message": "Resource not found"
    }


@product.delete("/<int:product_id>")
def delete(product_id: int):
    if product_service.delete(product_id):
        return {
            "status_code": 200,
            "message": "Success"
        }
    return {
        "status_code": 406,
        "message": "Error"
    }
