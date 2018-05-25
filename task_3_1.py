# 1


list_a = ['ab', 'ac', 'ad', 'bb', 'bc', 'bd']

# 2


list_b = list_a[:: 2]

# 3


list_c = [str(i) + 'a' for i in range(1, 5)]

# 4


list_c.remove('2a')
print(list_c)

# 5


list_c2 = list_c[:]  # or
list_c2 = list_c.copy()
list_c2.insert(1, '2a')
print(list_c2)
