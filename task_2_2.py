item_dollars = int(input('Enter item price - dollars, for example, 3: '))
item_cents = int(input('Enter item price - cents, for example, 20: '))
items_brought = int(input('Enter items brought, for example, 5: '))
ttl_cost = (item_dollars + item_cents/100) * items_brought
print('Total price is ', ttl_cost, '.', sep='')
