from NormalItem import Item, NormalItem

class Conjured(NormalItem):
    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)
    def updateItem(self):
        self.setSellIn()
        if self.sell_in > 0:
            self.setQuality(-2)
        else:
            self.setQuality(-4)


if __name__ == '__main__':
    ConjuredManaCake = Conjured("Conjured Mana Cake", 8, 30)
    print(ConjuredManaCake)
    dia = 0
    for i in range(31):
        ConjuredManaCake.updateItem()
        print('Dia ' + str(dia) + ': ' + str(ConjuredManaCake))
        dia = dia + 1