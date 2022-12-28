def read_file(filename):
    f = open(filename, "r", encoding="utf-8")
    data = f.read()
    f.close()

    return data


def write_file(filename, sentences_list):
    with open(filename, "w") as file:
        for line in sentences_list:
            file.write(line + '\n')


def get_beginning_values():
    return "", 0


def preprocess_data(data: str, max_len: int):
    data = data.replace("\n", "")
    data_list = data.split()

    result_list = []
    current_string, current_len = get_beginning_values()
    for current_word in data_list:
        if current_len + len(current_word) > max_len:
            result_list.append(current_string)
            current_string, current_len = get_beginning_values()
            current_string = current_word
            current_len = len(current_word)
        else:
            if current_string:
                current_string += " " + current_word
                current_len += len(current_word) + 1
            else:
                current_string = current_word
                current_len = len(current_word)

    result_list.append(current_string)
    return result_list


input_file = "input_sentences.txt"
output_file = "output_sentences.txt"
data = read_file(input_file)
max_length = 12
processed_data = preprocess_data(data, max_length)
write_file(output_file, processed_data)
