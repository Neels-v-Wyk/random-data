import json
import matplotlib.pyplot as plt

HOW_MANY_TOP_WORDS = 10

# Using a json -> dict is faster than a list of strings
with open('words_dictionary.json') as words_file:
    data = json.load(words_file)
    no_vowel_data = {}

    # Remove all vowels from all words
    for word in data:
        new_word = word

        for vowel in ['a', 'e', 'i', 'o', 'u']:
            if vowel in new_word:
                new_word = new_word.replace(vowel, '')

        if len(new_word) > 0:
            if new_word in no_vowel_data:
                no_vowel_data[new_word] += 1
            else:
                no_vowel_data[new_word] = 1

    sorted_vowel_data = dict(sorted(no_vowel_data.items(), key=lambda item: item[1]))

    top_list = {k: sorted_vowel_data[k] for k in list(sorted_vowel_data)[len(sorted_vowel_data) - HOW_MANY_TOP_WORDS:]}
    
    words = list(top_list.keys())
    occurences = list(top_list.values())
    
    plt.barh(range(len(top_list)), occurences, tick_label=words)
    plt.savefig('how-many-words-without-vowels.png', bbox_inches='tight')
    plt.show()
