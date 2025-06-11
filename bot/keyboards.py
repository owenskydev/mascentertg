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
        [InlineKeyboardButton("Категория 1", callback_data='category_1')],
        [InlineKeyboardButton("Категория 2", callback_data='category_2')],
        [InlineKeyboardButton("Категория 3", callback_data='category_3')],
        [InlineKeyboardButton("⬅️ Назад", callback_data='back')],
    ]
    return InlineKeyboardMarkup(keyboard)
