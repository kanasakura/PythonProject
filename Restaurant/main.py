from order import *
from menu_table import *

print('＜＜メニューを表示します＞＞')

display_all_menu('お肉', display_menu_table(meats))
display_all_menu('サイド', display_menu_table(sides))

print('=========================')

# 注文処理
meat_total_price, meat_count, meat_menu = food_order('お肉', meats)
side_total_price, side_count, side_menu = food_order('サイド', sides)

print('注文の品は' + meat_menu + str(meat_count) + '個・' + side_menu + str(side_count) + '個です。')

TAX = 1.08
total_price = round((meat_total_price + side_total_price) * TAX)

print('合計金額は：¥' + str(total_price) + '(税込)です')