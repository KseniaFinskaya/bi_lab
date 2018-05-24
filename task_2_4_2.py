input_text = str(input('Paste text: '))
input_pop_words = str(input('Type list of words to count from text: '))
input_text = input_text.lower()
input_text_l = input_text.split(' ')
input_pop_words_l = input_pop_words.split(' ')
dict_out = {}
for input_pop_word in input_pop_words_l:
    dict_out[input_pop_word] = input_text_l.count(input_pop_word)
print(dict_out)
