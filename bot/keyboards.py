from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def main_menu_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton("Каталог товаров", callback_data='catalog')],
        [InlineKeyboardButton("Оформить заказ", callback_data='order')],
        [InlineKeyboardButton("Связаться с оператором", url='https://t.me/safety1337')],
        [InlineKeyboardButton("О компании", callback_data='about')],
    ]
    return InlineKeyboardMarkup(keyboard)

def back_button_keyboard() -> InlineKeyboardMarkup:
    keyboard = [[InlineKeyboardButton("⬅️ Назад", callback_data='back')]]
    return InlineKeyboardMarkup(keyboard)

def catalog_categories_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton("Порционные весы(фасовочные)", callback_data='category_1')],
        [InlineKeyboardButton("Торговые весы", callback_data='category_2')],
        [InlineKeyboardButton("Счётные весы", callback_data='category_3')],
        [InlineKeyboardButton("Товарные весы", callback_data='category_4')],
        [InlineKeyboardButton("Платформенные весы", callback_data='category_5')],
        [InlineKeyboardButton("Фасовочные весы", callback_data='category_6')],
        [InlineKeyboardButton("Запчасти", callback_data='category_7')],
        [InlineKeyboardButton("Индикаторы", callback_data='category_8')],
        [InlineKeyboardButton("⬅️ Назад", callback_data='back')],
    ]
    return InlineKeyboardMarkup(keyboard)

# Словарь с товарами по категориям
CATEGORY_PRODUCTS = {
    "category_1": [
        ("ProMAS_PM4P", "product_pm4p"),
        ("ProMAS_PM4PHS", "product_pm4phs"),
        ("ProMAS_PM4R", "product_pm4r"),
        ("ProMAS_PM4U", "product_pm4u"),
    ],
    # Остальные категории пока пустые или заглушки
    "category_2": [
    ("MASter_MR1p", "product_mr1p"),
    ("MASter_MR1", "product_mr1"),
    ],
    "category_3": [
    ("MASter MC2", "product_mc2"),
    ],
    "category_4": [
    ("ProMAS_PM1E", "product_pm1e"),
    ("ProMAS_PM1B", "product_pm1b"),
    ("ProMAS_PM1H", "product_pm1h"),
    ("ProMAS_PM1HWS", "product_pm1hws"),
    ("ProMAS_PM1B-150M", "product_pm1b_150m"),
    ],
    "category_5": [
    ("ProMAS_PM4Pp", "product_pm4pp"),
    ('ProMAS_PM4PHp', "product_pm4php"),
    ('ProMAS_PM4Rp', "product_pm4rp"),
    ('ProMAS_PM4Up', 'product_pm4up'),
    ('ProMAS_PM4Tp', 'product_pm4tp'),
    ],
    "category_6": [
    ("PM1E_2828", "product_pm1e2828"),
    ("PM1E_3040", "product_pm1e3040"),
    ("PM1B_2828", "product_pm1b2828"),
    ("PM1B_3040", "product_pm1b3040"),
    ("PM1H_2828", "product_pm1h2828"),
    ("PM1H_3040", "product_pm1h3040"),
    ("PM1HWS_2828", "product_pm1hws2828"),
    ("PM1HWS_3040", "product_pm1hws3040"),
    ],
    "category_7": [("MSC", "product_MSC"),
    ("MS", "product_MS"),
    ("MI-E", "product_mi-e"),
    ("MI-B", "product_mi-b"),
    ("MI-H", "product_mi-h"),
    ("PM1E", "product_pm1e"),
    ("PM1-B", "product_pm1b"),
    ("PM1-H", "product_pm1h"),
    ],
    "category_8": [("MI-E", "product_mi-e"),
    ("MI-B", "product_mi-b"),
    ("MI-H", "product_mi-h"),
    ],
}

def category_products_keyboard(category: str) -> InlineKeyboardMarkup:
    products = CATEGORY_PRODUCTS.get(category, [("Товары скоро появятся", "no_product")])
    keyboard = [[InlineKeyboardButton(name, callback_data=cb)] for name, cb in products]
    keyboard.append([InlineKeyboardButton("⬅️ Назад", callback_data='back_to_categories')])
    return InlineKeyboardMarkup(keyboard)

def get_product_name(callback_data: str) -> str:
    for products in CATEGORY_PRODUCTS.values():
        for name, cb in products:
            if cb == callback_data:
                return name
    return "Товар"
