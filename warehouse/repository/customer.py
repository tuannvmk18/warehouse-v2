import sys

from sqlmodel import Session, select
from warehouse import engine
from warehouse.model import Customer
from warehouse.utils import update_model


def create(customer: Customer):
    with Session(engine) as session:
        session.add(customer)
        session.commit()
        session.refresh(customer)
        return customer


def get_all(litmit: int = sys.maxsize, offset: int = 1):
    with Session(engine) as session:
        statement = select(Customer).limit(litmit).offset(offset)
        results = session.exec(statement)
        customers = results.fetchall()
        return customers


def get_by_id(customer_id: int):
    with Session(engine) as session:
        statement = select(Customer).where(Customer.id == customer_id)
        results = session.exec(statement)
        customer = results.one_or_none()
        return customer


def delete(customer_id: int):
    with Session(engine) as session:
        statement = select(Customer).where(Customer.id == customer_id)
        customer = session.exec(statement).one_or_none()
        session.delete(customer)
        session.commit()
        return True
    return False


def update(customer_id: int, customer_update):
    with Session(engine) as session:
        statement = select(Customer).where(Customer.id == customer_id)
        customer = session.exec(statement).one_or_none()
        if customer is None:
            return None
        update_model(customer, customer_update)
        session.add(customer)
        session.commit()
        session.refresh(customer)
        return customer
