#Imported Restaurant:
from Ice_Cream_Stand_9_6 import Restaurant, IceCreamStand

restaurant = Restaurant('Bode Assado das Gêmeas', 'Bode Assado')

print(restaurant.name)
print(restaurant.type)
print(restaurant.number_served)

barraca_sorvete = IceCreamStand('Zecas', 'Sorveteria')
#restaurant.set_number_served(20)
#restaurant.increment_number_served(10)
#print(restaurant.number_served)
barraca_sorvete.list_icecream_flavors()