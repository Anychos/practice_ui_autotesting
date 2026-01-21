from enum import Enum


class Routes(str, Enum):
    HOME = "/"
    REGISTRATION = "/register"
    LOGIN = "/login"
    WISHLIST = "/wishlist"
    CART = "/cart"
