from NormalItem import Item, NormalItem

class AgedBrie(NormalItem):
    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)
    def updateItem(self):
        self.setSellIn()
        if self.sell_in > 0:
            self.setQuality(1)
        else:
            self.setQuality(2)


if __name__ == '__main__':
    Brie = AgedBrie("Aged Brie", 0, 0)
    print(Brie)
    dia = 0
    for i in range(31):
        Brie.updateItem()
        print('Dia ' + str(dia) + ': ' + str(Brie))
        dia = dia + 1