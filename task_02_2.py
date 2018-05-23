""" Task "Purchase money calculation": Write a program to calculate total cost.
One item costs M dollars and N cents. Customer bought L items.
Print total price in dollars and cents for L items."""


item_price = input('Enter item price, for example, 3.20: ')
items_brought = input('Enter items brought, for example, 5: ')
ttl_cost = float(item_price)*int(items_brought)
print('Total price is ', ttl_cost, '.', sep='')
