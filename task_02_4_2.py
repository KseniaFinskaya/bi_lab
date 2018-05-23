""" Task "Popular Words":
In this mission your task is to determine the popularity of certain words in the text.
At the input of your function are given 2 arguments: the text and the array of words
the popularity of which you need to determine.
When solving this task pay attention to the following points:
The words should be sought in all registers. This means that if you need to find a word "one" then words like "one",
"One", "oNe", "ONE" etc. will do.
The search words are always indicated in the lowercase.
If the word wasn’t found even once, it has to be returned in the dictionary with 0 (zero) value.
Input: The text and the search words array.
Output: The dictionary where the search words are the keys and values are the number of times when those words are
occurring in a given text."""


input_text = str(input('Paste text: '))
input_pop_words = str(input('Type list of words to count from text: '))
input_text = input_text.lower()
input_text_l = input_text.split(' ')
input_pop_words_l = input_pop_words.split(' ')
dict_out = {}
for input_pop_word in input_pop_words_l:
    dict_out[input_pop_word] = input_text_l.count(input_pop_word)
print(dict_out)
