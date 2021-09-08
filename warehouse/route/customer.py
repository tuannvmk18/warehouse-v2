import json

from flask import Blueprint
from flask import request
from warehouse.service import customer as customer_service

customer = Blueprint('customer_route', __name__)


@customer.get("/")
def get_all():
    limit = request.args.get('limit')
    offset = request.args.get('offset')
    return {
        "status_code": 200,
        "customers": json.loads(json.dumps(customer_service.get_all(limit, offset)))
    }


@customer.post("/")
def create_new():
    customer_json = customer_service.create(request.get_json())
    if customer_json is not None:
        return {
            "status_code": 200,
            "customer": json.loads(json.dumps(customer_json))
        }
    return {
        "status_code": 404,
        "message": "Resource not found"
    }


@customer.patch("/")
def patch():
    payload = dict(request.json)
    customer_id = payload.pop('id', None)
    customer_json = customer_service.update(customer_id, payload)
    if customer_json is not None:
        return {
            "status_code": 200,
            "customer": json.loads(json.dumps(customer_json))
        }
    return {
        "status_code": 404,
        "message": "Resource not found"
    }


@customer.get("/<int:customer_id>")
def get_by_id(customer_id: int):
    customer_json = customer_service.get_by_id(customer_id)
    if customer_json is not None:
        return {
            "status_code": 200,
            "customer": json.loads(json.dumps(customer_json))
        }
    return {
        "status_code": 404,
        "message": "Resource not found"
    }


@customer.delete("/<int:customer_id>")
def delete(customer_id: int):
    if customer_service.delete(customer_id):
        return {
            "status_code": 200,
            "message": "Success"
        }
    return {
        "status_code": 406,
        "message": "Error"
    }
