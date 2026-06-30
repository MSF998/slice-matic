"""
settings.py
-----------
Single source of truth for every constant, path, and magic variable in
the SliceMatic / PizzaFlow system.

Validation rules, pricing coefficients, log schema, and UI branding all
live here so that changing any rule means editing exactly one file.
"""

import os
import re

# ----------------------------------------------------------------------
# Paths
# ----------------------------------------------------------------------

# Project root = parent of this file's directory (config/)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_DIR = os.path.join(BASE_DIR, "data")
LOGS_DIR = os.path.join(BASE_DIR, "logs")

DEFAULT_LOG_PATH = os.path.join(LOGS_DIR, "orders_log.txt")

MENU_FILES = {
    "base":    os.path.join(DATA_DIR, "Types_of_Base.txt"),
    "pizza":   os.path.join(DATA_DIR, "Types_of_Pizza.txt"),
    "topping": os.path.join(DATA_DIR, "Types_of_Toppings.txt"),
}

# ----------------------------------------------------------------------
# Customer validation
# ----------------------------------------------------------------------

NAME_MIN_LEN    = 2
NAME_MAX_LEN    = 40
NAME_RE         = re.compile(r"^[A-Za-z ]+$")

PHONE_LEN         = 10
PHONE_VALID_START = ("6", "7", "8", "9")

# ----------------------------------------------------------------------
# Order / quantity constraints
# ----------------------------------------------------------------------

LINE_QTY_MIN  = 0    # 0 = "not ordering this pizza" on its row
LINE_QTY_MAX  = 10   # max units of a single pizza type per order
TOTAL_QTY_MAX = 10   # hard per-order capacity ceiling (sum across all lines)

TOPPING_QTY_MIN = 0  # 0 = topping not added to this pizza
TOPPING_QTY_MAX = 5  # max extra servings of one topping per pizza unit

# ----------------------------------------------------------------------
# Pricing
# ----------------------------------------------------------------------

DISCOUNT_THRESHOLD = 5     # total pizzas in cart that triggers discount
DISCOUNT_RATE      = 0.10  # 10% off pre-GST subtotal
GST_RATE           = 0.18  # 18% on post-discount amount

# ----------------------------------------------------------------------
# Payment
# ----------------------------------------------------------------------

PAYMENT_MODES = {1: "Cash", 2: "Card", 3: "UPI"}

# ----------------------------------------------------------------------
# Log format -- field order governs serialisation and deserialisation
# Level separators: | (order fields) ; (lines) : (line sub-fields) + (toppings) x (topping qty)
# ----------------------------------------------------------------------

ORDER_FIELD_ORDER = [
    "timestamp", "customer_name", "phone",
    "items", "subtotal", "discount", "gst", "final_total", "payment_mode",
]

LINE_FIELD_ORDER = [
    "pizza_id", "pizza_name", "base_id", "base_name", "base_price",
    "pizza_price", "quantity", "toppings", "line_subtotal",
]

# ----------------------------------------------------------------------
# UI branding (Gradio app)
# ----------------------------------------------------------------------

NAVY = "#1A1A2E"
PINK = "#C2185B"

_CW = "https://commons.wikimedia.org/wiki/Special:FilePath/"
PIZZA_IMAGES = {
    "Margherita":        _CW + "Pizza%20Margherita%20-%20San%20Francisco%2C%20CA.jpg?width=500",
    "Chicago Deep Dish": _CW + "Giordano%27s%20Chicago%20Deep%20Dish%20Pizza.jpg?width=500",
    "California Veggie": _CW + "Vegetable%20pizza%20Denpasar%20Bali.JPG?width=500",
    "Pepperoni Classic": _CW + "Pepperoni%20pizza.jpeg?width=500",
    "BBQ Chicken":       _CW + "BBQ%20Chicken%20Pizza%20Hut.jpg?width=500",
}
FALLBACK_IMAGE = _CW + "Supreme%20pizza.jpg?width=500"
