def order_menu_count():
    while True:
        try:
            while True:
                order_count = int(input('いくつ注文しますか？(上限注文数10個)：'))

                if order_count > 10:
                    print('上限注文数10個を超えています!!')
                elif order_count < 0:
                    print('負の値は使用できません')
                else:
                    return order_count

        except ValueError:
            print('エラー：数字以外の文字を入力しないで〜(泣)')


def food_order(food, category):
    while True:
        try:
            menu_number = int(input(f'{food}の番号を選択してください：'))

            if 0 <= menu_number < len(category):
                selected_menu = category[menu_number]
                print(f'{selected_menu.name}が選択されました')
                food_count = order_menu_count()
                category_total_price = selected_menu.get_total_price(food_count)

                return [category_total_price, food_count, selected_menu.name]
            else:
                print('メニュー番号がありません')

        except ValueError:
            print('エラー：数字以外の文字を入力しないで〜(泣)')
