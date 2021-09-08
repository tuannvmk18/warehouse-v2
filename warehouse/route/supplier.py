import json

from flask import Blueprint
from flask import request
from warehouse.service import supplier as supplier_service

supplier = Blueprint('supplier_route', __name__)


@supplier.get("/")
def get_all():
    limit = request.args.get('limit')
    offset = request.args.get('offset')
    return {
        "status_code": 200,
        "data": json.loads(json.dumps(supplier_service.get_all(limit, offset)))
    }


@supplier.post("/")
def create_new():
    supplier_json = supplier_service.create(request.get_json())
    if supplier_json is not None:
        return {
            "status_code": 200,
            "data": json.loads(json.dumps(supplier_json))
        }
    return {
        "status_code": 404,
        "message": "Resource not found"
    }


@supplier.patch("/")
def patch():
    payload = dict(request.json)
    supplier_id = payload.pop('id', None)
    supplier_json = supplier_service.update(supplier_id, payload)
    if supplier_json is not None:
        return {
            "status_code": 200,
            "data": json.loads(json.dumps(supplier_json))
        }
    return {
        "status_code": 404,
        "message": "Resource not found"
    }


@supplier.get("/<int:supplier_id>")
def get_by_id(supplier_id: int):
    supplier_json = supplier_service.get_by_id(supplier_id)
    if supplier_json is not None:
        return {
            "status_code": 200,
            "data": json.loads(json.dumps(supplier_json))
        }
    return {
        "status_code": 404,
        "message": "Resource not found"
    }


@supplier.delete("/<int:supplier_id>")
def delete(supplier_id: int):
    if supplier_service.delete(supplier_id):
        return {
            "status_code": 200,
            "message": "Success"
        }
    return {
        "status_code": 406,
        "message": "Error"
    }
