import json
from datetime import datetime

from warehouse.repository import order as order_repository
from warehouse.repository import product as product_repository
from warehouse.model import Product, Order, OrderProductLink
from warehouse.utils import update_model


def get_full(order_id: int):
    order_repository.get_full_oder(order_id)


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
