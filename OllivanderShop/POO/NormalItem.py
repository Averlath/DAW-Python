class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class Interfaz:
    def updateItem(self):
        """ Como cada Item tiene un comportamiento diferente creamos una clase abstracta"""
        pass

class NormalItem(Item, Interfaz):
    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)
    def setSellIn(self):
        self.sell_in -= 1
    def setQuality(self, valor):
        if self.quality + valor > 50:
            self.quality = 50
        elif self.quality + valor >= 0:
            self.quality += valor
        else:
            self.quality = 0
    def updateItem(self):
        self.setSellIn()
        if self.sell_in > 0:
            self.setQuality(-1)
        else:
            self.setQuality(-2)
    def getName(self):
        return self.name
    def getQuality(self):
        return self.quality
    def getSellIn(self):
        return self.sell_in

    """ Clase NormalItem: todos los objetos que no tienen caracteristicas especiales serán creadas con  estas clase"""    

if __name__ == '__main__':
    """ Compruebo que los item se crean en el formato correcto"""
    NZoth = Item("N'Zoth", 50, 50)
    assert NZoth.name == "N'Zoth"
    Tyrion = NormalItem("Tyrion Fordring", 0, 40)
    assert Tyrion.quality == 40
    print(Tyrion.getName())
    print(Tyrion.getQuality())
    
    """ Casos Test UpdateItem"""
    ThaurissanCard = NormalItem ("Emperor Thaurissan", 9, 10)
    assert ThaurissanCard.sell_in == 9
    assert ThaurissanCard.quality == 10
    ThaurissanCard.updateItem()
    assert ThaurissanCard.sell_in == 8
    assert ThaurissanCard.quality == 9