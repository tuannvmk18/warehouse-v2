import json

from flask import Blueprint
from flask import request
from warehouse.service import order as order_service

order = Blueprint('order_route', __name__)


@order.post("/")
def create():
    order_service.create(request.json)
    return "OK"


@order.get("/<int:order_id>")
def get(order_id: int):
    order_service.get_full(order_id)
    return "OK"
