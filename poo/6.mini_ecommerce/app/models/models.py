from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Boolean, Float, Integer, String, SmallInteger
from app.db.db import Base


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String(45))


class Supplier(Base):
    __tablename__ = "suppliers"

    id = Column(Integer, primary_key=True)
    name = Column(String(45))


class PaymentMethod(Base):
    __tablename__ = "payment_methods"

    id = Column(Integer, primary_key=True)
    name = Column(String(45))
    enabled = Column(Boolean)


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    description = Column(String(150))
    price = Column(Float(10, 2))
    technical_details = Column(String(255))
    image = Column(String(255))
    visible = Column(Boolean, default=True)

    category_id = Column(Integer, ForeignKey(Category.id))
    category = relationship(Category)
    supplier_id = Column(Integer, ForeignKey(Supplier.id))
    supplier = relationship(Supplier)


class ProductDiscount(Base):
    __tablename__ = "product_discounts"

    id = Column(Integer, primary_key=True)
    value = Column(Float(10, 2))
    mode = Column(String(15))

    payment_method_id = Column(Integer, ForeignKey(PaymentMethod.id))
    payment_method = relationship(PaymentMethod)
    product_id = Column(Integer, ForeignKey(Product.id))
    product = relationship(Product)
