from menu_basis import MenuBasis


class Meats(MenuBasis):
    def __init__(self, name, price, amount):
        super().__init__(name, price)
        self.amount = amount

    def display(self):
        return f'{self.name}: ¥{str(self.price)}({str(self.amount)}g)'
