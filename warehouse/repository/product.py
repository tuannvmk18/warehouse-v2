from sqlmodel import Session, select
from warehouse import engine
from warehouse.model import Product
from warehouse.utils import update_model


def get_all():
    with Session(engine) as session:
        statement = select(Product)
        results = session.exec(statement)
        products = results.fetchall()
        return products


def get_by_id(product_id: int):
    with Session(engine) as session:
        statment = select(Product).where(Product.id == product_id)
        results = session.exec(statment)
        product = results.one_or_none()
        return product


def create(product_create: Product):
    with Session(engine) as session:
        session.add(product_create)
        session.commit()
        session.refresh(product_create)
        return product_create


def get_by_supplier_id(supplier_id: int):
    with Session(engine) as session:
        statement = select(Product).where(Product.supplier_id == supplier_id)
        results = session.exec(statement)
        products = results.fetchall()
        return products


def delete_by_id(product_id: int):
    with Session(engine) as session:
        statement = select(Product).where(Product.id == product_id)
        results = session.exec(statement)
        product = results.one_or_none()
        print(product)
        if product is None:
            return False

        session.delete(product)
        session.commit()
        return True


def update(product_id: int, product_update: dict):
    with Session(engine) as session:
        statement = select(Product).where(Product.id == product_id)
        results = session.exec(statement)
        product = results.one_or_none()

        if product is None:
            return None

        update_model(product, product_update)

        session.add(product)
        session.commit()
        session.refresh(product)
        return product
