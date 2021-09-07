import json

from warehouse.repository import product as product_repository
from warehouse.model import Product
from warehouse.utils import update_model

import sys


def get_all(limit: int = sys.maxsize, offset: int = 1):
    products = [json.loads(product.json()) for product in product_repository.get_all(limit, offset)]
    return products


def get_by_id(product_id):
    product = product_repository.get_by_id(product_id)
    if product is not None:
        return json.loads(product.json())
    return None


def create(data):
    product_create = Product()
    update_model(product_create, data)
    product = product_repository.create(product_create)
    if product is not None:
        return json.loads(product.json())
    return None


def delete(product_id: int):
    is_delete_success = product_repository.delete_by_id(product_id)
    return is_delete_success


def update(product_id: int, product_update):
    product = product_repository.update(product_id, product_update)
    if product is not None:
        return json.loads(product.json())
    return None
