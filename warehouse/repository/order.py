import json
import sys
from typing import List

from sqlmodel import Session, select
from warehouse import engine
from warehouse.model import Product, Order, OrderProductLink, Customer


def get_all(limit: int = sys.maxsize, offset: int = 1):
    results = []
    with Session(engine) as session:
        statement = select(Order).limit(limit).offset(offset)
        orders = session.exec(statement).fetchall()

        for o in orders:
            results.append(get_full_oder(o.id))
        return results


def create(order: Order):
    with Session(engine) as session:
        session.add(order)
        session.commit()
        session.refresh(order)
        return order


def get_full_oder(order_id):
    result = {'cart': []}
    with Session(engine) as session:
        o = session.exec(select(Order).where(Order.id == order_id)).one()
        ll = session.exec(select(OrderProductLink).where(OrderProductLink.order_id == order_id)).fetchall()
        c = session.exec(select(Customer).where(Customer.id == o.customer_id)).one()
        total = 0
        for ol in ll:
            p = session.exec(select(Product).where(Product.id == ol.product_id)).one()
            op = json.loads(p.json())
            op['amount'] = ol.amount
            op['p_total'] = p.price * ol.amount
            total += op['p_total']
            result['cart'].append(op)
        result['total'] = total
        result['order_id'] = o.id
        result['order_date'] = o.order_date.strftime('%H:%M:%S %d/%m/%Y')
        result['customer_name'] = c.name
        result['customer_address'] = c.address
        result['customer_phone'] = c.phone
    return result


def create_orderlink(order: Order, order_links: List[OrderProductLink]):
    with Session(engine) as session:
        session.add(order)
        session.refresh(order)
        for o in order_links:
            session.add(o)

        session.commit()
        return order
