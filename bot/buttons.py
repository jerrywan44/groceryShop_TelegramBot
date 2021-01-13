from bot.config import about_path as gh_rm
import bot.sql.sql_utils as db

from aiogram.types import ReplyKeyboardRemove, \
        ReplyKeyboardMarkup, KeyboardButton, \
        InlineKeyboardMarkup, InlineKeyboardButton

# 2 level with sqlite db
def categ_menu():
    markup_categ = InlineKeyboardMarkup(row_width=3)
    for category in db.show_categories():
        btn_categ = InlineKeyboardButton(category[1], callback_data='categ_id:' + str(category[0]))
        markup_categ.add(btn_categ)
    
    return markup_categ

# 1 level: menu
def main_menu():
    btn_categ = InlineKeyboardButton(text = 'Категории', callback_data='categ') 
    global btn_cart
    btn_cart = InlineKeyboardButton(text = 'Корзина', callback_data='cart') 
    btn_about = InlineKeyboardButton(text = 'Информация', url = gh_rm, callback_data='about') 
    btn_exit = InlineKeyboardButton(text = 'Выход', callback_data='exit')

    markup_menu = InlineKeyboardMarkup()
    markup_menu.row(btn_categ).row(btn_cart) # add categories and cart
    markup_menu.row(btn_about, btn_exit) # add about and exit bot ?

    return markup_menu
'''
# 2 level: categories
def categ_menu():
    btn_sales = InlineKeyboardButton('Скидки!', callback_data='sales') 
    btn_drinks = InlineKeyboardButton('Напитки', callback_data='drinks') 
    btn_veg = InlineKeyboardButton('Овощи', callback_data='veg')
    btn_fruits = InlineKeyboardButton('Фрукты', callback_data='fruits')
    btn_milk = InlineKeyboardButton('Молоко', callback_data='milk')
    btn_bread = InlineKeyboardButton('Хлеб', callback_data='water')
    btn_meat = InlineKeyboardButton('Мясо', callback_data='meat')
    btn_fish = InlineKeyboardButton('Рыба', callback_data='fish')
    btn_cereal = InlineKeyboardButton('Бакалея', callback_data='cereal')
    btn_back_categ = InlineKeyboardButton('Назад', callback_data='back_categ')

    markup_categ = InlineKeyboardMarkup(row_width=3)
    markup_categ.add(btn_sales, btn_drinks, btn_veg, btn_fruits,  # add all categories
    btn_milk, btn_bread, btn_meat, btn_fish, btn_cereal)
    markup_categ.row(btn_back_categ)

    return markup_categ
'''
# 3 level: specific product
def product_menu():
    btn_incr = InlineKeyboardButton('-', callback_data='decr')
    btn_decr = InlineKeyboardButton('+', callback_data='incr')
    btn_addcart = InlineKeyboardButton('В корзину', callback_data='addcart')
    btn_back_product = InlineKeyboardButton('Назад', callback_data='back_product')

    markup_product = InlineKeyboardMarkup().row(btn_incr, btn_decr) # add '+' and '-'
    markup_product.row(btn_addcart) # add to cart
    markup_product.row(btn_back_product) # add back and cart

    return markup_product

# cart
def cart_menu():
    btn_place = InlineKeyboardButton('Оформить заказ на', callback_data='place_order') # + srt (sum)
    '''
    btn_left = InlineKeyboardButton('<', callback_data='left') # flipping
    btn_quantity = InlineKeyboardButton('', callback_data='quantity') # to add pages
    btn_right = InlineKeyboardButton('>', callback_data='right')
    '''
    btn_empty_cart = InlineKeyboardButton('Очистить', callback_data='empty')
    btn_back_cart = InlineKeyboardButton('К товарам', callback_data='back_cart')

    markup_cart = InlineKeyboardMarkup(row_width=1)
    markup_cart.add(btn_place, btn_empty_cart, btn_back_cart)

    return markup_cart