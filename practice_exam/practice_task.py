#Написать функцию, которая принимает на вход имя файла и порождает ленивый генератор,
#вывести при помощи него все слова, в которых не менее 2 гласных. Если слово оканчивается на пунктационный символ,
#то есть разделение слов типа ", " и так далее, убирать символы в конце строки. Файл закрыть.


punctuations = [",", ".", ":", ";", "!", "?"]


def count_vowels(check_word):
    return len([letter for letter in check_word if letter.lower() in 'aeiouауеояиюэ'])


def read_file(filename):
    f = open(filename, "r", encoding="utf-8")
    data = f.read()
    f.close()

    return data


def delete_ending_punctuations(word_to_delete):
    while word_to_delete[-1] in punctuations:
        word_to_delete = word_to_delete[:-1]

    return word_to_delete


def process_data(data):
    data_list = data.split()
    for current_word in data_list:
        current_word = delete_ending_punctuations(current_word)
        count_v = count_vowels(current_word)
        if count_v > 1:
            yield current_word


input_file = "input.txt"
file_data = read_file(input_file)
words = process_data(file_data)
for word in words:
    print(word)





