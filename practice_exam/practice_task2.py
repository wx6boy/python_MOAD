def read_file(filename):
    f = open(filename, "r", encoding="utf-8")
    data = f.read()
    data = data.replace("\n", " ")
    f.close()

    return data


def write_file(filename, string_to_write):
    with open(filename, "w") as file:
        file.write(string_to_write)


def get_beginning_values():
    return "", 0


def preprocess_data(data: str, max_len: int):
    data_list = data.split()

    result_list = []
    current_string, current_len = get_beginning_values()
    for current_word in data_list:
        if current_len + len(current_word) + 1 > max_len:
            result_list.append(current_string)
            current_string = current_word
            current_len = len(current_word)
        else:
            if current_string:
                current_string += " " + current_word
                current_len += len(current_word) + 1
            else:
                current_string = current_word
                current_len = len(current_word)

    result_string = "\n".join(result_list)
    return result_string


input_file = "input_sentences2.txt"
output_file = "output_sentences.txt"
data = read_file(input_file)
max_length = 8
result_string = preprocess_data(data, max_length)
write_file(output_file, result_string)
