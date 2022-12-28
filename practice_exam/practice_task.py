punctuations = [",", ".", ":", ";", "!", "?"]


def count_vowels(check_word):
    return len([letter for letter in check_word if letter.lower() in 'aeiouауеояиюэ'])


def function_process(filename):
    f = open(filename, "r", encoding="utf-8")
    data = f.read()
    data_list = data.split()
    for current_word in data_list:
        while current_word[-1] in punctuations:
            current_word = current_word[:-1]
        count_v = count_vowels(current_word)
        if count_v > 1:
            yield current_word
    f.close()


input_file = "input.txt"
words = function_process(input_file)
for word in words:
    print(word)





