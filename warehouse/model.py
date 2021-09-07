from datetime import datetime
from typing import List, Optional

from sqlmodel import SQLModel, Field, Relationship


class OrderProductLink(SQLModel, table=True):
    __tablename__ = "order_detail"
    order_id: Optional[int] = Field(default=None, foreign_key="order.id", primary_key=True)
    product_id: Optional[int] = Field(default=None, foreign_key="product.id", primary_key=True)
    amount: int


class Order(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    order_date: datetime
    products: List["Product"] = Relationship(back_populates="orders", link_model=OrderProductLink)


class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: str
    supplier_id: Optional[int] = Field(default=None, foreign_key="supplier.id")
    orders: List[Order] = Relationship(back_populates="products", link_model=OrderProductLink)


class Supplier(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    address: str
    phone: str


class Customer(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    address: Optional[str] = Field(default=None)
    phone: Optional[str] = Field(default=None)
    gender: Optional[str] = Field(default=None)
    email: str
