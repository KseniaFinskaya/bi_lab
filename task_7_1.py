# 1
import re


pattern = r'\S+@\S+\.\S+'
text = 'ksenia@tut.by load fnb@google.com'

for match in re.findall(pattern, text):
    print(match)


# 2
pattern = r'\b\D{3,5}\b'
text = 'true two sixth process'
for word in re.findall(pattern, text):
    print(word)


# 3
pattern = r'\d+'
text = 'two 2 five 5'
list1 = []
for match in re.findall(pattern, text):
    list1.append(match)
print(list1)


# 4
pattern = r'\s'
replace_pattern = r'_'
pattern2 = r' '
text = 'ksenia test python'
undescore_text = re.sub(pattern, replace_pattern, text)
print(undescore_text)
wh_text = re.sub(replace_pattern, pattern2, undescore_text)
print(wh_text)
