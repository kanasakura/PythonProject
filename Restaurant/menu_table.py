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
    result = []
    for index, food in enumerate(category):
        result.append(f'{str(index)}.{food.display()}')
    return result


# 内包表記.ver
# def display_menu_table2(category):
#    return [f'{str(index)}.{food.display()}' for index, food in enumerate(category)]


# 全てのメニューを表示
def display_all_menu(food, display_menu):
    print('-------[' + food + 'メニュー]--------')
    for menu in display_menu:
        print(menu)
