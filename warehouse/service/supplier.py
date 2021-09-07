import json

from warehouse.repository import supplier as supplier_repository
from warehouse.model import Supplier
from warehouse.utils import update_model

import sys


def get_all(limit: int = sys.maxsize, offset: int = 1):
    suppliers = [json.loads(supplier.json()) for supplier in supplier_repository.get_all(limit, offset)]
    return suppliers


def get_by_id(supplier_id):
    supplier = supplier_repository.get_by_id(supplier_id)
    if supplier is not None:
        return json.loads(supplier.json())
    return None


def create(data):
    supplier_create = Supplier()
    update_model(supplier_create, data)
    supplier = supplier_repository.create(supplier_create)
    if supplier is not None:
        return json.loads(supplier.json())
    return None


def delete(supplier_id: int):
    is_delete_success = supplier_repository.delete_by_id(supplier_id)
    return is_delete_success


def update(supplier_id: int, supplier_update):
    supplier = supplier_repository.update(supplier_id, supplier_update)
    if supplier is not None:
        return json.loads(supplier.json())
    return None
