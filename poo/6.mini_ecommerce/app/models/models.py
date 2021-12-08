from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Boolean, Date, DateTime, Float, Integer, String
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
    created_at = Column(DateTime)

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


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    display_name = Column(String(45))
    email = Column(String(45), unique=True)
    role = Column(String(15))
    password = Column(String(45))


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(45))
    last_name = Column(String(45))
    phone_number = Column(String(15))
    genre = Column(String(45))
    document_id = Column(String(45))
    birth_date = Column(Date)
    user_id = Column(Integer, ForeignKey(User.id))
    user = relationship(User)


class Address(Base):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True)
    address = Column(String(255))
    city = Column(String(45))
    state = Column(String(2))
    number = Column(String(10))
    zipcode = Column(String(6))
    neighbourhood = Column(String(45))
    primary = Column(Boolean, default=True)

    customer_id = Column(Integer, ForeignKey(Customer.id))
    customer = relationship(Customer)


class Coupon(Base):
    __tablename__ = "coupons"

    id = Column(Integer, primary_key=True)
    code = Column(String(10), unique=True)
    expire_at = Column(DateTime)
    limit = Column(Integer)
    type = Column(String(15))
    value = Column(Float(10, 2))
