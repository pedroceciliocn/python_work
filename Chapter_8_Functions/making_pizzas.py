import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra chesse')



#or importing specific functions
## from module_name import function_name
## from module_name import function_0, function_1, function_2

from pizza import make_pizza

make_pizza(18, 'pepperoni')
make_pizza(14, 'tomate', 'cebola', 'pimentao')

#or using as to give a function an alias
## from module_name import function_name as fn
from pizza import make_pizza as mp

mp(20, 'salame')
mp(10, 'calabresa', 'cheese')

#or using as to give a module an alias
## import module_name as mn
import pizza as p

p.make_pizza(8, 'catupiry')
p.make_pizza(22, 'provoloni', 'cheddar')

#or importing all functions in a module
## from module_name import *
from pizza import *
make_pizza(18, 'pepperoni')
make_pizza(14, 'tomate', 'cebola', 'pimentao')