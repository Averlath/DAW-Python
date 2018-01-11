from NormalItem import Item, NormalItem

class BackstagePass(NormalItem):
    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)
    def updateItem(self):
        self.setSellIn()
        if self.sell_in <= 0:
            self.quality = 0
        elif self.sell_in <= 5:
            self.setQuality(3)
        elif self.sell_in <= 10:
            self.setQuality(2)
        else:
            self.setQuality(1)


if __name__ == '__main__':
    TAFKAL80ETC = BackstagePass("Backstage passes to a TAFKAL80ETC concert", 15, 5)
    print(TAFKAL80ETC)
    dia = 0
    for i in range(31):
        TAFKAL80ETC.updateItem()
        print('Dia ' + str(dia) + ': ' + str(TAFKAL80ETC))
        dia = dia + 1