from enum import Enum


class Routes(str, Enum):
    HOME = "/"
    REGISTRATION = "/register?returnUrl=%2F"
    LOGIN = "/login?returnUrl=%2F"
    WISHLIST = "/wishlist"
    CART = "/cart"
    ACCOUNT = "/customer/info"
