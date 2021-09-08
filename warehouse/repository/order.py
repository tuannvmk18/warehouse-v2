from typing import List

from sqlmodel import Session, select
from warehouse import engine
from warehouse.model import Product, Order, OrderProductLink
from warehouse.utils import update_model
import sys


def get_all():
    with Session(engine) as session:
        statement = select(Product)
        results = session.exec(statement)
        orders = results.fetchall()
        return orders


def create(order: Order):
    with Session(engine) as session:
        session.add(order)
        session.commit()
        session.refresh(order)
        return order


def get_full_oder(order_id):
    query = "SELECT * FROM \"order\" as o, order_detail as od, product as p WHERE o.id = od.order_id AND p.id = od.product_id and order_id = 3"
    with Session(engine) as session:
        # statement = select(Order, Product).join(Product).where(Order.id == order_id)
        results = session.exec(query)
        print(results.fetchall())


def create_orderlink(order: Order, order_links: List[OrderProductLink]):
    with Session(engine) as session:
        session.add(order)
        session.refresh(order)
        for o in order_links:
            session.add(o)

        session.commit()
        return order
