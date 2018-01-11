from NormalItem import Item, NormalItem

class Sulfuras(NormalItem):
    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)
    def setQuality(self, valor):
        self.quality = 80
        assert self.quality == 80



if __name__ == '__main__':
    Sulfuras = Sulfuras("Sulfuras, Hand of Ragnaros", 0, 80)
    print(Sulfuras)
    dia = 0
    for i in range(31):
        Sulfuras.updateItem()
        print('Dia ' + str(dia) + ': ' + str(Sulfuras))
        dia = dia + 1