import json

from flask import Blueprint
from flask import request
from warehouse.service import order as order_service

order = Blueprint('order_route', __name__)


@order.get("/")
def get_all():
    limit = request.args.get("litmit")
    offset = request.args.get("offset")
    data = order_service.get_all(limit, offset)
    return {
        "status_code": 200,
        "data": data
    }


@order.post("/")
def create():
    order_service.create(request.json)
    return "OK"


@order.get("/<int:order_id>")
def get(order_id: int):
    response = order_service.get_full(order_id)
    return {
        "status_code": 200,
        "data": response
    }
