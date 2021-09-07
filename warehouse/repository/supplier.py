import sys

from sqlmodel import Session, select
from warehouse import engine
from warehouse.model import Supplier
from warehouse.utils import update_model


def get_all(limit: int = sys.maxsize, offset: int = 1):
    with Session(engine) as session:
        statement = select(Supplier).limit(limit).offset(offset)
        results = session.exec(statement)
        suppliers = results.fetchall()
        return suppliers


def get_by_id(supplier_id: int):
    with Session(engine) as session:
        statement = select(Supplier).where(Supplier.id == supplier_id)
        results = session.exec(statement)
        supplier = results.one_or_none()
        return supplier


def create(supplier_create: Supplier):
    with Session(engine) as session:
        session.add(supplier_create)
        session.commit()
        session.refresh(supplier_create)
        return supplier_create


def delete(supplier_id: int):
    with Session(engine) as session:
        statement = select(Supplier).where(Supplier.id == supplier_id)
        results = session.exec(statement)
        supplier = results.one_or_none()

        if supplier is None:
            return False

        session.delete(supplier)
        session.commit()
        return True


def update(supplier_id: int, supplier_update: dict):
    with Session(engine) as session:
        statement = select(Supplier).where(Supplier.id == supplier_id)
        results = session.exec(statement)
        supplier = results.one_or_none()

        if supplier is None:
            return None

        update_model(supplier, supplier_update)
        session.add(supplier)
        session.commit()
        session.refresh(supplier)
        return supplier
