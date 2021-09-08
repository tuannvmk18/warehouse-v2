import json
import sys
from datetime import datetime

from warehouse.repository import order as order_repository
from warehouse.repository import product as product_repository
from warehouse.model import Order, OrderProductLink


def get_full(order_id: int):
    result = order_repository.get_full_oder(order_id)
    return result


def get_all(limit: int = sys.maxsize, offset: int = 1):
    results = order_repository.get_all(limit, offset)
    return results


def create(data):
    order = Order()
    order_links = []
    order.order_date = datetime.now()
    order.customer_id = data['customer_id']
    order = order_repository.create(order)

    for p in data['list_product']:
        product = product_repository.get_by_id(p['id'])
        order_link = OrderProductLink(product=product, order=order, amount=p['amount'])
        order_links.append(order_link)

    order_repository.create_orderlink(order, order_links)
