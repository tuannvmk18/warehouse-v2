import json
import sys

from warehouse.repository import customer as customer_repository
from warehouse.model import Customer
from warehouse.utils import update_model


def get_all(limit: int = sys.maxsize, offset: int = 1):
    customer = [json.loads(customer.json()) for customer in customer_repository.get_all(limit, offset)]
    return customer


def get_by_id(customer_id):
    customer = customer_repository.get_by_id(customer_id)
    if customer is not None:
        return json.loads(customer.json())
    return None


def create(data):
    customer_create = Customer()
    update_model(customer_create, data)
    customer = customer_repository.create(customer_create)
    if customer is not None:
        return json.loads(customer.json())
    return None


def delete(customer_id: int):
    is_delete_success = customer_repository.delete(customer_id)
    return is_delete_success


def update(customer_id: int, customer_update):
    customer = customer_repository.update(customer_id, customer_update)
    if customer is not None:
        return json.loads(customer.json())
    return None
