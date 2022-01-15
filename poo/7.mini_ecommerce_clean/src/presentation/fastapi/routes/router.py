from fastapi import APIRouter
from src.presentation.fastapi.routes.product_route import router as product_router
from src.presentation.fastapi.routes.product_route import router as product_router
from src.presentation.fastapi.routes.product_route import router as product_router
from src.presentation.fastapi.routes.product_route import router as product_router
from src.presentation.fastapi.routes.product_route import router as product_router
from src.presentation.fastapi.routes.product_route import router as product_router

router = APIRouter()

router.include_router(product_router, prefix='/products', tags=['product'])
router.include_router(product_router, prefix='/categories', tags=['category'])
router.include_router(product_router, prefix='/suppliers', tags=['supplier'])
router.include_router(product_router, prefix='/coupons', tags=['coupon'])
router.include_router(
    product_router, prefix='/payment_methods', tags=['payment_method'])
router.include_router(
    product_router, prefix='/product_discounts', tags=['product_discount'])
