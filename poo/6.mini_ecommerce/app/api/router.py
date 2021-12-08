from fastapi import APIRouter
from .category.views import router as category_router
from .supplier.views import router as supplier_router
from .payment_method.views import router as payment_method_router
from .product.views import router as product_router
from .product_discount.views import router as product_discount_router
from .coupon.views import router as coupon_router
from .customer.views import router as customer_router
from .address.views import router as address_router
from .admin.views import router as admin_router


router = APIRouter()

router.include_router(category_router, prefix="/category", tags=['category'])

router.include_router(supplier_router, prefix="/supplier", tags=['supplier'])

router.include_router(
    payment_method_router, prefix="/payment-method", tags=['payment-method']
)

router.include_router(product_router, prefix="/product", tags=['product'])

router.include_router(
    product_discount_router, prefix="/product-discount", tags=['product-discount']
)

router.include_router(
    coupon_router, prefix="/coupon", tags=['coupon']
)

router.include_router(
    customer_router, prefix="/customer", tags=['customer']
)

router.include_router(
    address_router, prefix="/address", tags=['address']
)

router.include_router(
    admin_router, prefix="/admin", tags=['admin']
)
