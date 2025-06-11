from telegram import Update
from telegram.ext import ContextTypes
from bot.keyboards import (
    main_menu_keyboard,
    back_button_keyboard,
    catalog_categories_keyboard,
    category_products_keyboard,
    get_product_name,
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Выбери действие ниже:",
        reply_markup=main_menu_keyboard()
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == 'catalog':
        text = "Выберите категорию товаров:"
        reply_markup = catalog_categories_keyboard()

    elif data.startswith("category_"):
        text = "Выберите товар:"
        reply_markup = category_products_keyboard(data)

    elif data.startswith("product_"):
        product_name = get_product_name(data)
        text = f"<b>{product_name}</b>\nИнформация пока недоступна, будет позже."
        reply_markup = back_button_keyboard()

    elif data == 'back_to_categories':
        text = "Выберите категорию товаров:"
        reply_markup = catalog_categories_keyboard()

    elif data == 'order':
        text = "Здесь оформление заказа."
        reply_markup = back_button_keyboard()

    elif data == 'about':
        text = (
            "<b>О компании MAS-center</b>\n"
            "MAS-center производит, продаёт и обслуживает качественное весоизмерительное оборудование "
            "для разных отраслей: торговля, питание, производство, логистика, строительство, сельское хозяйство и др.\n\n"
            "Наш бренд MAS™ гарантирует высокое качество: все модели проходят разработку, тестирование и сертификацию "
            "по российским стандартам.\n\n"
            "Продукция производится в России и на ведущих фабриках мира, известных в своей отрасли."
        )
        reply_markup = back_button_keyboard()

    elif data == 'back':
        text = "Привет! Выбери действие ниже:"
        reply_markup = main_menu_keyboard()

    else:
        text = "Неизвестная команда."
        reply_markup = back_button_keyboard()

    await query.edit_message_text(text, reply_markup=reply_markup, parse_mode="HTML")
