
from src.domain.product.model import Product
from src.domain.category.model import Category
from src.domain.supplier.model import Supplier
from src.domain.coupon.model import Coupon
from src.domain.payment_method.model import PaymentMethod
from src.domain.product_discount.model import ProductDiscount
from src.domain.customer.model import Customer
from src.domain.address.model import Address

from src.adapter.database import Session
from src.adapter.orm import start_mapper
from src.services.sqlalchemy_uow import SqlAlchemyUnitOfWork


start_mapper()
uow = SqlAlchemyUnitOfWork()

s = Supplier("supplier 1")
c = Category("category 1")

with uow:
    a = uow.supplier_repository.add(s)
    b = uow.category_repository.add(c)

    uow.commit()

# category_repository = CategoryRepository(db)
# category = Category(
#     name='categoria 1'
# )
# category_repository.add(category)
# print(category.id, category.name)


# supplier_repository = SupplierRepository(db)
# supplier = Supplier(
#     name='fornecedor 1'
# )
# supplier_repository.add(supplier)
# print(supplier.id, supplier.name)


# payment_method_repository = PaymentMethodRepository(db)
# payment_method = PaymentMethod(
#     name='Pix', enabled=True
# )
# payment_method_repository.add(payment_method)
# print(payment_method.id, payment_method.name)


# product_repository = ProductRepository(db)
# product = Product(
#     description='descricao 2', price=10.0,
#     technical_details='detalhes tecnicos', image='', visible=True, category=category, supplier=supplier
# )


# product_discount_repository = ProductDiscountRepository(db)
# product_discount = ProductDiscount(
#     mode='percentage', value=15.80, payment_method=payment_method
# )

# product.add_discount(product_discount)
# product_repository.add(product)


# print(product.id, product.description)
# print(product_discount.id, product_discount.value)


# coupon_repository = CouponRepository(db)
# coupon = Coupon(
#     code='XXX', expire_at=None,
#     limit=5, type='percentage', value=50
# )
# coupon_repository.add(coupon)
# print(coupon.id, coupon.code)


# customer_repository = CustomerRepository(db)
# customer = Customer(
#     first_name="Victor", last_name="Piassi", phone_number="1999999999", genre="Masc", document_id="123123432", birth_date=None
# )


# address_repository = AddressRepository(db)
# address = Address(
#     address="Test Street1", city="Testcity", state="Test state", number="666", zipcode="123456", neighbourhood="Test district", primary=True
# )
# address2 = Address(
#     address="Test Street2", city="Testcity", state="Test state", number="666", zipcode="123456", neighbourhood="Test district", primary=True
# )


# # COMPORTAMENTO ESTRANHO

# customer.add_address(address)

# customer.add_address(address2)

# c = customer_repository.add(customer)

# print(customer.id, customer.first_name)
# print(address.id, address.primary, address.customer_id)
