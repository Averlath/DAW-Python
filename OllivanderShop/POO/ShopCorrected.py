from NormalItem import Item, NormalItem
from AgedBrie import AgedBrie
from Sulfuras import Sulfuras
from BackstagePass import BackstagePass
from Conjured import Conjured

DexterityVest = NormalItem("+5 Dexterity Vest", 10, 20)
AgedBrie = AgedBrie("Aged Brie", 2, 0)
ElixirOfTheMongoose = NormalItem("Elixir of the Mongoose", 5, 7)
SulfurasTwo = Sulfuras("Sulfuras, Hand of Ragnaros", 0, 80)
Sulfuras = Sulfuras("Sulfuras, Hand of Ragnaros", -1, 80)
Concert = BackstagePass("Backstage passes to a TAFKAL80ETC concert", 15, 20)
ConcertTwo = BackstagePass("Backstage passes to a TAFKAL80ETC concert", 10, 49)
ConcertThree = BackstagePass("Backstage passes to a TAFKAL80ETC concert", 5, 49)
ConjuredManaCake = Conjured("Conjured Mana Cake", 3, 6)

items = [DexterityVest, AgedBrie, ElixirOfTheMongoose, Sulfuras, SulfurasTwo, Concert, ConcertTwo, ConcertThree, ConjuredManaCake]

print('Initial Cases')
print('---------------')
for element in items:
	print(element)
print('---------------')
dia = 0
for i in range(30):
	print('-' * 5 + 'Dia ' + str(dia) + '-' * 5)
	for element in items:
		element.updateItem()
		print(element)
	dia = dia + 1