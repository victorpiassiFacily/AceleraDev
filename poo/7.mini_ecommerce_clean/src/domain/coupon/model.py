class Coupon:
    def __init__(self, code, expire_at, limit, type, value):
        self.code = code
        self.expire_at = expire_at
        self.limit = limit
        self.type = type
        self.value = value
