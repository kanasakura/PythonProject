from menu_basis import MenuBasis
from meats import Meats

# 肉テーブル
meat1 = Meats('特上牛タン', 1000, 200)
meat2 = Meats('カルビ', 300, 150)
meat3 = Meats('ロース', 280, 100)
meat4 = Meats('ハラミ', 350, 100)
meat5 = Meats('鶏モモ', 250, 90)

meats = [meat1, meat2, meat3, meat4, meat5]

# サイドテーブル
side1 = MenuBasis('シーザーサラダ', 400)
side2 = MenuBasis('ライス', 250)
side3 = MenuBasis('ビビンバ', 500)
side4 = MenuBasis('じゃがバター焼き', 300)
side5 = MenuBasis('玉子スープ', 400)

sides = [side1, side2, side3, side4, side5]


# カテゴリーごとのメニューを配列に入れる
def display_menu_table(category):
    index = 0
    result = []
    for food in category:
        result.append(str(index) + '.' + food.display())
        index += 1
    return result


# 全てのメニューを表示
def display_all_menu(food, display_menu):
    print('-------[' + food + 'メニュー]--------')
    for menu in display_menu:
        print(menu)